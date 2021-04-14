import numpy as np
def modified_black_body(wl, TEMPSN, RADIUSSN, TEMPDUST, MDUST):
    # 2components BlackBody formula
    h = 6.626076e-27  # plancks constant (erg s)
    k = 1.38066e-16  # boltzmann constant (erg/K)
    BETAL = 1.5  # slope for kappa
    MSUN = 1.98892e+33  # g
    CC = 2.99792458E+10  # cm/s

    wlCM = wl * 1e-8  # wavelength from Angstrom to cm
    B1 = 2 * h * (CC ** 2)  ##erg cm^2 s^-1
    B2 = h * CC / k  # K cm

    BX = (B1 / wlCM ** 5)  # erg s^-1 cm^-3
    #     BX=BX*1e-8 #convert from [erg s^-1 cm^-3] to [erg s^-1 cm^2 A^-1]


    #########change the D value to the distance of the source from observer
    D = 45.7  # Mpc
    LDS = D * 3.086e+18 * 1e+6  # luminosity distance from Mpc to cm

    KAPPASIN = 1e+4 * (wlCM / 1e-4) ** (
        -BETAL)  # [cm^2 g^-1]normalised to wavelength 1000. nm in cm #1 nm = 1.E-7 cm

    flux_sn = BX / ((np.exp(B2 / (wlCM * TEMPSN))) - 1)  # erg s^-1 cm^-3
    flux_snA = np.pi * flux_sn * (((RADIUSSN ** 2)) / (LDS ** 2))  # erg s^-1 cm^-3
    flux_sn_erg = flux_snA * 1e-8  # convert now from [erg s^-1 cm^-3] to [erg s^-1 cm^2 A-1]



    flux_d = (BX / ((np.exp(B2 / (wlCM * TEMPDUST))) - 1))
    flux_dA = flux_d * KAPPASIN * ((MDUST * MSUN) / (LDS ** 2))
    flux_d_erg = flux_dA * 1e-8  # convert now from [erg s^-1 cm^-3] to [erg s^-1 cm^2 A-1]


    flux = (flux_sn_erg + flux_d_erg)
    max_flux=np.max(flux)

    return flux #, max_flux