import numpy as np
import pandas as pd
from scipy.optimize import least_squares


def apprendre_modele_thermique(calibration):
    """
    Apprend la relation entre température externe et interne.

    calibration : DataFrame contenant les colonnes
        'Température externe'
        'Température interne'

    Retourne les paramètres a, b et g.
    """
    Te = calibration["Température externe"].to_numpy(dtype=float)
    Ti = calibration["Température interne"].to_numpy(dtype=float)

    masque = np.isfinite(Te) & np.isfinite(Ti)
    Te, Ti = Te[masque], Ti[masque]

    if len(Te) < 4:
        raise ValueError("Pas assez de mesures de calibration.")

    # Paramètres du modèle :
    # Ti[n] = a*Ti[n-1] + (1-a)*(b + g*Te[n-1])

    def residus(params):
        a, b, g = params
        prediction = a * Ti[:-1] + (1 - a) * (
            b + g * Te[:-1]
        )
        return Ti[1:] - prediction

    resultat = least_squares(
        residus,
        x0=[0.9, 0.0, 1.0],
        bounds=([0.0, -np.inf, -np.inf],
                [0.99999, np.inf, np.inf])
    )

    a, b, g = resultat.x

    return {"a": a, "b": b, "g": g}


def estimer_temperature_interne(
    temperatures_externes,
    modele,
    temperature_initiale=None
):
    """
    Transforme un vecteur de températures externes
    en vecteur de températures internes estimées.

    Les mesures doivent être régulièrement espacées.
    """
    Te = np.asarray(temperatures_externes, dtype=float)

    if Te.ndim != 1:
        raise ValueError("Le vecteur doit être à une dimension.")

    if not np.all(np.isfinite(Te)):
        raise ValueError("Les températures contiennent des valeurs manquantes.")

    a, b, g = modele["a"], modele["b"], modele["g"]

    Ti = np.empty_like(Te)

    if len(Te) == 0:
        return Ti

    if temperature_initiale is None:
        Ti[0] = b + g * Te[0]
    else:
        Ti[0] = temperature_initiale

    for n in range(1, len(Te)):
        Ti[n] = (
            a * Ti[n-1]
            + (1-a) * (b + g * Te[n-1])
        )

    return Ti


def apprendre_modele_pression(calibration, modele_thermique):
    """
    Apprend la sensibilité thermique de la pression
    à partir des données de calibration.
    """
    Te = calibration["Température externe"].to_numpy(dtype=float)
    Ti_reelle = calibration["Température interne"].to_numpy(dtype=float)
    P = calibration["Pression"].to_numpy(dtype=float)

    masque = np.isfinite(Te) & np.isfinite(Ti_reelle) & np.isfinite(P)
    Te, Ti_reelle, P = Te[masque], Ti_reelle[masque], P[masque]

    # On estime la température interne avec le modèle thermique.
    Ti_estimee = estimer_temperature_interne(
        Te,
        modele_thermique,
        temperature_initiale=Ti_reelle[0]
    )

    # Régression de la pression sur la température interne.
    X = np.column_stack([
        np.ones(len(Ti_estimee)),
        Ti_estimee
    ])

    c, k = np.linalg.lstsq(X, P, rcond=None)[0]

    return {
        "c": c,
        "k": k,
        "T_ref": np.mean(Ti_estimee)
    }


def corriger_pression(
    calibration,
    pressions_reelles,
    temperatures_externes_reelles,
    temperature_initiale=None
):
    """
    Corrige la pression mesurée sur le terrain.

    Retourne un vecteur de pression corrigée.
    """
    modele_thermique = apprendre_modele_thermique(calibration)

    modele_pression = apprendre_modele_pression(
        calibration,
        modele_thermique
    )

    P = np.asarray(pressions_reelles, dtype=float)
    Te = np.asarray(temperatures_externes_reelles, dtype=float)

    if P.shape != Te.shape:
        raise ValueError("Les vecteurs de pression et de température doivent avoir la même taille.")

    Ti = estimer_temperature_interne(
        Te,
        modele_thermique,
        temperature_initiale
    )

    k = modele_pression["k"]
    T_ref = modele_pression["T_ref"]

    pression_thermique = k * (Ti - T_ref)

    pression_corrigee = P - pression_thermique

    return pression_corrigee

data = pd.read_excel('/Users/apoure/Documents/Molonari/calib/test_5h_calibration.xlsx')

print(apprendre_modele_thermique(data))