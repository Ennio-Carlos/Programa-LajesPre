import math
from math import ceil
from math import floor
class Dimensionamento():
    def __init__(self):
        self.funcoes = {
            'bf': self.bf,
            'bw': self.bw,
            'pp_c': self.pp_c,
            'p_total': self.p_total,
            'acidental': self.acidental,
            'vao_livre': self.vao_livre,
            'vao_comprimento': self.vao_comprimento,
            'momento_pos_biapoiado': self.momento_pos_biapoiado,
            'd': self.d,
            #'momento_biengastado': self.momento_biengastado,
            #'momento_engastadoeapoiado': self.momento_engastadoeapoiado,
            'd0': self.d0,
            'kmd': self.kmd,
            'kx': self.kx,
            'as_total': self.as_total,
            'as_adicional': self.as_adicional,
            'Vk': self.Vk,
            'trd': self.trd,
            'k': self.k,
            'p1': self.p1,
            'Vrd1': self.Vrd1,
            'alpha_v1': self.alpha_v1,
            'Vrd2': self.Vrd2,
# Momento na alma
            'M1': self.M1,
            'M2': self.M2,
            'kmd2': self.kmd2,
            'kx2': self.kx2,
            'As_1': self.As_1,
            'As_2': self.As_2,
            'as_total2': self.as_total2,
            'as_adicional2': self.as_adicional2,

            'p_total_els': self.p_total_els,
            'mk_els': self.mk_els,
            'fctm': self.fctm,
            'Ic': self.Ic,
            'ag': self.ag,
            'ycg': self.ycg,
            'Mr': self.Mr,
            'a1': self.a1,
            'Ecs': self.Ecs,
            'a2': self.a2,
            'a3': self.a3,
            'yii': self.yii,
            'Iii_mesa': self.Iii_mesa,
            'Iii_alma': self.Iii_alma,
            'EI_eq': self.EI_eq,
            'w0': self.w0,
            't0': self.t0,
            'ksi_t0': self.ksi_t0,
            'alpha_f': self.alpha_f,
            'flecha_total': self.flecha_total,
            'area_bitola': self.area_bitola,
            'quantidade_barras': self.quantidade_barras,
            'pmin': self.pmin,
            'as_min': self.as_min,
# Quantitativo
            'por_enchimento': self.por_enchimento,
            'volume': self.volume,
            'vigota': self.vigota,
            'lajota_1': self.lajota_1,
            'lajota_2': self.lajota_2,
            'quantidade_lajota': self.quantidade_lajota,
            'quantidade_aco': self.quantidade_aco,
            'flecha_lim': self.flecha_lim,
            'contra_flecha': self.contra_flecha





            #'As_minima': self.As_minina,
            #'p_mim': self.p_min

        }
# Dimensionamento linha neutra na mesa
    def bf(self, be, ah, bv):
        return ((be-(2*ah)+bv))
    def bw(self, bv, ah):
        return (bv-(2*ah))
    def pp_c(self, capa, bf, hb, bw, ah, av, be, b):
        return ((capa*bf) + (hb*bw) + (ah*av*2))*0.25 + ((be*(hb-av))+((be-2*ah)*av))*b/10000#kgf/m
    def p_total (self, pp_c, r, q, bf):
        return ((pp_c + r*bf/100)+ q*bf/100)#kgf/m
    def acidental (self, q):
        return (q*1)
    def vao_livre (self, l):
        return (l*1)
    def vao_comprimento (self, c):
        return (c*1)
    def momento_pos_biapoiado(self, p_total, l):
        return (((p_total)*((l/100)**2))/8)#kgf.m
    def d0(self, mk, fck, bf, capa):
        return ((mk*1.4)/(0.85*((fck/10)/1.4)*bf*capa))+(capa/2)
    def d(self, hb, av, capa, hv, cobrimento, phi_trelica):
        return (((hb-av)+hv+capa)-cobrimento-((phi_trelica/10)/2))
    def kmd(self, mk, bf, fck, d):
        return ((mk*1.4)/(bf*((fck/10)/1.4)*(d**2)))
    def kx(self, kmd):
        return (1.25 - 1.9174*(0.425-kmd)**(1/2))

    def as_total(self, mk, d, kx, fyk_trelica):
        return ((mk*100*1.4)/((1-0.4*kx)*d*(fyk_trelica*10)/1.15))

    def as_adicional(self, as_total, phi_trelica, fyk, fyk_trelica ):
        return (as_total-(2*(math.pi*(((phi_trelica/10)**2)/4))*(fyk_trelica/fyk)))
# Dimensionamento linha neutra na alma
#========================================================================
    def M1(self, fck, capa, bf, bw, d):
        return 0.85*((fck/10)/1.4)*capa*(bf-bw)*(d-(capa/2))/100

    def M2 (self, mk, M1):
        return ((mk/100*1.4)- M1)

    def kmd2 (self, M2, d, fck, bw):
        return ((M2*100)/((d**2)*((fck/10)/1.4*bw)))

    def kx2(self, kmd2):
        return (1.25 - 1.9174*(0.425-kmd2)**(1/2))

    def As_1(self, M1, d, capa, fyk_trelica):
        return ((M1*100)/((d-(0.5*capa))*((fyk_trelica/10)/1.15)))
    #N11*100/(Q11*E11*($B$4/10)/$B$6)+      M11*100/(E11-D11/2)/(($B$4/10)/$B$6);"lim x/d")

    def As_2(self, M2, kx2, d, fyk_trelica ):
        return ((M2*100)/((1-(0.4*kx2))*d*((fyk_trelica/10)/1.15)))

    def as_total2(self, As_1, As_2 ):
        return (As_1 + As_2)
    def as_adicional2(self, as_total_2, phi_trelica, fyk, fyk_trelica ):
        return (as_total_2-(math.pi*((phi_trelica/10)**2)/4)*(fyk_trelica/fyk))
    def pmin (self, fck, fyk):
        return ((0.0784*(fck**(2/3)))/((fyk)/1.15)) #tem quer ser maior de 15%
    def as_min (self, pmin, capa, bf, hb, bw):
        return (pmin*((capa*bf) + (hb*bw)))
# Cálculo da cortante
# ========================================================================
    def Vk (self, p_total, l):
        return (p_total * l/100)/2 #kgf/m
    def trd (self, fck):
        return (0.0375*(fck**(2/3)))*(10**5)
    def k (self, d):
        return (1.6-d/100)
    def p1 (self, as_total, bw, d):
        return (as_total/(bw*d))
    def Vrd1 (self, trd, k, p1, bw, d):
        return (trd*k*(1.2+40*p1)*(bw/100)*(d/100))
    def alpha_v1 (self, fck):
        return (0.7-fck/200)
    def Vrd2 (self, alpha_v1, fck, bw, d):
        return (0.5*alpha_v1*((fck*(10**5))/1.4)*(bw/100)*0.9*(d/100))
# Dimensionamento flechas
#========================================================================
    def p_total_els (self, pp_c, r, q, bf, psi2):
        return (pp_c + r*(bf/100)+ (q*((bf/100)*psi2)))#kgf/m/nerv
    def mk_els(self, p_total_els, l):
        return (((p_total_els)*((l/100)**2))/8)
    def fctm (self, fck):
        return ((0.3*fck**(2/3))*10)#kgf/cm2
    def ag (self, bf, bw, capa, hb, av, hv):
        return ((bf-bw)*capa+bw*(((hb-av)+hv)+capa))
    def ycg (self, capa, bf, bw, hb, hv, av, ag):
        return ((bf-bw)*((capa**2)/2)+(bw*((((hb-av)+hv)+capa)**2)/2))/ag
    def Ic (self, bf, bw, capa, hb, hv, ycg, av):
        return (((bf-bw)*capa**3)/12)+((bw*(((hb-av)+hv)+capa)**3)/12)+(bf-bw)*capa*(ycg-(capa/2))**2+bw*(((hb-av)+hv)+capa)*(ycg-((((hb-av)+hv)+capa)/2))**2
    def Mr (self, fctm, Ic, hb, hv, ycg, av, capa):
        return ((1.2*fctm*Ic/((((hb-av)+hv)+capa)-ycg)/100))#kgf.m
    def a1 (self, bw):
        return ((bw)/2)
    def Ecs (self, fck):
        return ((0.8+0.2*(fck/80))*(5600*(fck**0.5)))
    def a2 (self, capa, bf, bw, Ecs, as_total):
        return (capa*(bf-bw)+(2100000/(Ecs*10))*as_total)
    def a3 (self, d, Ecs, as_total, capa, bf, bw):
        return (-d*((2100000/(Ecs*10))*as_total) - ((capa**2)/2)*(bf-bw))
    def yii (self, a1, a2, a3):
        return (-a2+((a2**2)-(4*a1*a3))**0.5)/(2*a1)
    def Iii_mesa (self, bf, yii, Ecs, as_total, d):
        return (((bf*(yii**3))/3)+(2100000/(Ecs*10))*as_total*(d-yii)**2)
    def Iii_alma (self, bf, bw, capa, yii, Ecs, as_total, d):
        return ((((bf-bw)*capa**3)/12)+((bw*yii**3)/3)+(bf-bw)*capa*((yii-(capa/2))**2)+(2100000/(Ecs*10))*as_total*((d-yii)**2))
    def EI_eq (self, Ecs, Mr, mk_els, Ic, Iii):
        return Ecs*10*(((Mr/mk_els)**3)*Ic+(1-((Mr/mk_els)**3))*Iii)
    def w0 (self, alpha_c, p_total_els, l, EI_eq):
        return ((alpha_c*(p_total_els/100)*(l**4))/EI_eq)
    def t0 (self, dias):
        return (dias/30)#dias
    def ksi_t0 (self, t0):
        return 0.68*(0.996**t0)*t0**0.32
    def alpha_f (self, ksi_t0):
        return (2 - ksi_t0)
    def flecha_total (self, w0, alpha_f):
        return (w0*(1+alpha_f))
    def flecha_lim (self, l):
        return l/250
    def contra_flecha (self, flecha_total, l):
        return (flecha_total-(l/250))
#combinações
    #def permanente (self, pp_c, r, bf):
     #   return (pp_c + r*(bf/100))
    #def quase_permanente (self, pp_c, r, q, bf, psi2):
     #   return (pp_c + r*(bf/100)+ (q*((bf/100)*psi2)))
    #def rara (self, pp_c, r, q, bf):
    #    return (pp_c + r*(bf/100)+ (q*((bf/100))))
    #def Mat(self, depnde, l):
    #    return (((depnde)*((l/100)**2))/8)
    #def ei_eq (self, Ecs, Mr, Mat, Ic, Iii):
    #    return Ecs*10*(((Mr/Mat)**3)*Ic+(1-((Mr/Mat)**3))*Iii)
    #def flecha_por_combinação (self, alpha_c, combinação, l, EI_eq):
    #    return ((alpha_c*(combinação/100)*(l**4))/EI_eq)
# Bitola
# ========================================================================
    def area_bitola (self, d ):
        return (math.pi*((d/10)**2))/(4)
    def quantidade_barras (self, as_adicional, area_bitola):
        return ceil((as_adicional / area_bitola))
# Quantitativo
#========================================================================
    def por_enchimento (self, be, ah, hb, capa, bv):
        return (((be-ah)*hb)/(hb+capa)/((be-ah)+bv))
    def volume (self, c, l, por, hb, capa):
        return ((hb+capa)/100*(1-por)*((c*l)/10000))
    def vigota (self, bv, be, ah, c):
        return ceil((c/((bv)+(be-2*ah))))
    def lajota_1 (self, bv, be, ah, c):
        return floor((c/((bv)+(be-2*ah))))
    def lajota_2 (self, l, ce):
        return floor(l/ce)
    def quantidade_lajota(self, lajota_1, lajota_2):
        return (lajota_1*lajota_2)
    def quantidade_aco(self, l, peso):
        return (((l+10)/100)*peso)




if __name__ == '__main__':
    calculadora = Dimensionamento()


    alpha_v1 = calculadora.funcoes['alpha_v1'](20)
    print('Resultado é ', "%.5f" % alpha_v1)
    Vrd2 = calculadora.funcoes['Vrd2'](alpha_v1, 20, 9, 10)
    print('Resultado é ', "%.5f" % Vrd2)
