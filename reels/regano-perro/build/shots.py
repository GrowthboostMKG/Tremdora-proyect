# Montaje plano a plano. t = inicio en la línea de tiempo (s). El final de cada plano es el inicio del siguiente.
# src: prefijo del archivo subido. kind: v (vídeo) / p (foto).
# cx, cy: centro del encuadre 9:16 (fracción del área útil). z0 -> z1: zoom (1 = encuadre máximo).
# rect: recorte previo del área útil (x, y, w, h) para quitar barras/interfaz de las grabaciones.
END = 99.6
SHOTS = [
 dict(t=0.00,  src="c070233c", kind="v", cx=.50, cy=.50, z0=1.00, z1=1.05, note="Primer plano mirando a su persona: «Le has dicho ahora no»"),
 dict(t=5.60,  src="453521a3", kind="v", cx=.50, cy=.40, z0=1.22, z1=1.30, note="«Él no.» Asoma tras el sofá"),
 dict(t=9.75,  src="669e9476", kind="v", cx=.50, cy=.45, z0=1.00, z1=1.03, note="«Estás en el sofá con el móvil»"),
 dict(t=13.50, src="7ffe9edc", kind="p", cx=.40, cy=.52, z0=1.00, z1=1.07, note="«Él llega con su pelota» (IMG_7807)"),
 dict(t=16.75, src="3e4aaef5", kind="v", cx=.50, cy=.50, z0=1.02, z1=1.00, note="«Y tú la apartas»"),
 dict(t=20.25, src="fccc432a", kind="p", cx=.50, cy=.47, z0=1.06, z1=1.06, note="«Se queda quieto. Te mira.» plano quieto (IMG_7795)"),
 dict(t=23.15, src="0102aac9", kind="v", cx=.50, cy=.50, z0=1.00, z1=1.04, rect=(0,2,1206,1500), note="«Se tumba lejos, la cabeza entre las patas»"),
 dict(t=28.65, src="e6c7cab0", kind="v", cx=.50, cy=.48, z0=1.00, z1=1.04, note="«En Viena demostraron que los perros» perro escuchando"),
 dict(t="distinguen", src="5787177e", kind="p", cx=.55, cy=.48, z0=1.00, z1=1.06, note="«distinguen una cara enfadada» (IMG_7848)"),
 dict(t="de una alegre", src="1545372f", kind="v", cx=.50, cy=.45, z0=1.00, z1=1.04, note="«de una alegre»"),
 dict(t=34.95, src="353a53aa", kind="v", cx=.50, cy=.45, z0=1.00, z1=1.03, note="«Tu cara ya se lo ha dicho» mirada de reojo"),
 dict(t=39.55, src="262db733", kind="v", cx=.45, cy=.50, z0=1.00, z1=1.03, note="«Pero aquí no acaba la cosa»"),
 dict(t=42.15, src="f2076f8d", kind="v", cx=.50, cy=.50, z0=1.00, z1=1.00, inp=0.6, note="«Diez minutos después, vuelve»"),
 dict(t=46.35, src="5169b934", kind="p", cx=.58, cy=.50, z0=1.00, z1=1.07, note="«Apoya el hocico en tu pierna» (IMG_7794)"),
 dict(t=50.85, src="0852df01", kind="p", cx=.30, cy=.62, z0=1.04, z1=1.10, note="Suecia: el perro observa a su persona"),
 dict(t=55.95, src="af0af5ef", kind="v", cx=.50, cy=.50, z0=1.00, z1=1.03, note="«Si tú estás mal»"),
 dict(t=58.85, src="33ece1c9", kind="v", cx=.58, cy=.50, z0=1.00, z1=1.00, note="«Y viene a arreglarlo»"),
 dict(t=60.85, src="7a711a6b", kind="v", cx=.50, cy=.50, z0=1.00, z1=1.03, note="«Y hay un experimento…» laboratorio"),
 dict(t=65.05, src="687bc058", kind="p", cx=.55, cy=.50, z0=1.00, z1=1.07, note="«En Estados Unidos… detrás de una puerta» (IMG_7854)"),
 dict(t="fingiendo", src="fd456ac2", kind="p", cx=.58, cy=.45, z0=1.00, z1=1.06, note="«fingiendo llorar» (IMG_7849)"),
 dict(t=70.95, src="ca1dfecf", kind="v", cx=.50, cy=.50, z0=1.00, z1=1.03, note="«Sus perros corrían a abrirla…» perro que llega a la puerta"),
 dict(t=76.05, src="d8764c68", kind="p", cx=.42, cy=.45, z0=1.00, z1=1.06, note="«No te guarda rencor… solo sabe volver»"),
 dict(t=80.65, src="9a289c41", kind="p", cx=.50, cy=.40, z0=1.00, z1=1.10, note="«Él solo tiene una. Tú.»"),
 dict(t=85.85, src="9b940630", kind="p", cx=.50, cy=.50, z0=1.00, z1=1.06, note="«Así que suelta el móvil…» (IMG_7811)"),
 dict(t="lánzale", src="df5d231a", kind="v", cx=.50, cy=.50, z0=1.00, z1=1.00, inp=0.9, note="«…y lánzale esa pelota» jack russell con la pelota"),
 dict(t=89.05, src="370eb9ec", kind="v", cx=.50, cy=.50, z0=1.00, z1=1.05, rect=(0,10,1196,2122), note="Cierre juntos + pregunta + logo"),
]
