#!/usr/bin/env python3
"""Las cinco piezas extra de los packs."""
from complementos import pag, autora, cierre, lineas, escribir, EMBLEMA


def cubierta(pack, rotulo, titulo, sub, edi):
    return pag(f'''  <div class="pill">{pack} · {rotulo}</div>
  <div class="brandmark">TREMDORA</div>
  {EMBLEMA}
  <h1>{titulo}</h1>
  <div class="sub">{sub}</div>
  <div class="cv-foot">
    <div class="lbl">Forma parte del pack</div>
    <div class="names">{pack}</div>
    <div class="edi">{edi}</div>
  </div>''', "cover serie")


def ficha_rutina(num, nombre, cuando, pasos, clave=None, aviso=None):
    ps = "\n".join(f"    <li>{p}</li>" for p in pasos)
    extra = ""
    if clave:
        extra += f'''
  <div class="box">
    <span class="lbl">Por qué funciona</span>
    <p>{clave}</p>
  </div>'''
    if aviso:
        extra += f'''
  <div class="box warn">
    <span class="lbl">Ojo</span>
    <p>{aviso}</p>
  </div>'''
    return pag(f'''  <div class="wk-head">
    <div class="n">{num:02d}</div>
    <div class="t">{nombre}<span>{cuando}</span></div>
  </div>

  <ol class="pasos">
{ps}
  </ol>
{extra}''')


def tarjeta(num, nombre, dur, que, porque):
    return f'''  <div class="momento">
    <div class="mh"><span class="mn">{num:02d}</span><span class="mt">{nombre}</span><span class="md">{dur}</span></div>
    <p class="mq">{que}</p>
    <p class="mp"><b>Por qué:</b> {porque}</p>
  </div>'''


def pagina_momentos(titulo, intro, tarjetas):
    return pag(f'''  <div class="kicker">20 Momentos</div>
  <h1 class="ch-title">{titulo}</h1>
  <div class="ch-who">{intro}</div>

''' + "\n".join(tarjetas))


def carta(num, titulo, entrada, n_lineas):
    return pag(f'''  <div class="wk-head">
    <div class="n">{num:02d}</div>
    <div class="t">{titulo}<span>Carta de conexión</span></div>
  </div>

  <p class="lead">{entrada}</p>

{lineas(n_lineas)}''')


AUT_CORTA = '''  <p class="a-lead">Me llamo Victoria, tengo 44 años, y Tremdora existe por una perra que se llamaba Paris.</p>

  <p>Estuve <b>diecisiete años compitiendo con ella</b>. Madrugones, viajes, los nervios de antes de entrar, y la vuelta a casa las dos agotadas. Paris no fue mi mascota: fue mi compañera de equipo durante casi toda mi vida adulta.</p>

  <p>Y aun así, lo que más echo de menos no son las competiciones. Son <b>las tardes sin prisa</b>, que son justo las que fui dejando pasar pensando que ya habría un momento mejor. Ese momento no llega solo: se busca, o no pasa.</p>

  <p>Por eso cada cosa que hago en Tremdora intenta dejar también <b>una experiencia bonita de recordar</b>. Porque de todos estos años, lo que me queda no son los resultados: es lo que compartimos.</p>'''


# ══════════════════════════════════════════════ 1 · RUTINAS DE CALMA

RUT = [
    cubierta("Hogar en Calma", "Rutinas",
             "Rutinas de <em>Calma</em>",
             "Seis protocolos para imprimir y tener a mano: lo que hay que hacer, en orden, cuando no hay tiempo de pensar.",
             "Seis rutinas"),

    pag('''  <div class="kicker">Antes de empezar</div>
  <h1 class="ch-title">Para qué sirven estas seis hojas</h1>
  <div class="ch-who">Están pensadas para imprimirse y pegarse en la nevera</div>

  <p class="lead">Todo esto está explicado en <i>Hogar en Calma</i>. Aquí no hay nada nuevo: hay <b>seis protocolos sueltos</b>, uno por hoja, con los pasos en orden y sin el porqué. Para los momentos en que no hace falta entender nada, solo saber qué toca ahora.</p>

  <div class="box">
    <span class="lbl">Cómo usarlas</span>
    <p>Imprime las que te hagan falta y <b>déjalas donde vayan a servir</b>: la de la salida en la entrada, la de la noche de ruido en la cocina, la del veterinario dentro del transportín.</p>
    <p>Y enséñaselas a <b>quien más vaya a estar con tu mascota</b>: quien la cuide cuando no estés es quien más las necesita, y es el que nunca ha leído el libro.</p>
  </div>

  <div class="box warn">
    <span class="lbl">Una rutina no sustituye al trabajo</span>
    <p>Estas hojas <b>gestionan</b> el momento. No lo arreglan. Lo que de verdad cambia las cosas es el trabajo progresivo de los programas del libro, hecho en los días tranquilos — no en los días difíciles.</p>
  </div>'''),

    ficha_rutina(1, "La salida aburrida", "Cada vez que te vas de casa",
        ["Respira despacio un minuto <b>antes</b> de empezar a prepararte. Te está leyendo a ti.",
         "Deja el juguete relleno y congelado, o la comida escondida, <b>justo antes</b> de coger las llaves.",
         "Enciende un sonido de fondo constante y bajo: la radio vale.",
         "<b>Sal sin despedirte.</b> Ni voz aguda, ni caricias largas, ni «ya vuelvo».",
         "Al volver, entra en silencio y <b>espera unos segundos de calma</b> antes de saludarla."],
        clave="El contraste es lo que hace daño: cuanto más intenso es el reencuentro, más dura se hace la ausencia. Que irse y volver sea lo más aburrido del día."),

    ficha_rutina(2, "La noche de ruido", "Tormenta, petardos, obras",
        ["Habitación interior, <b>persianas bajadas</b> y un ruido de fondo constante.",
         "Deja que <b>elija ella dónde esconderse</b>, y no la saques de ahí para consolarla.",
         "Acompáñala con calma, sin dramatizar. Tu tensión también la lee.",
         "<b>No la saques a pasear</b> en horas de petardos, ni para hacer sus necesidades si puedes evitarlo.",
         "Comprueba que el <b>microchip y tus datos</b> están al día: son las noches con más animales perdidos del año."],
        clave="Esa noche solo se puede gestionar. Lo que de verdad lo cambia es la desensibilización, y se trabaja meses antes.",
        aviso="Si lo pasa muy mal cada año, <b>pide cita con margen</b>: hay tratamientos para esas noches y se preparan con tiempo, no el mismo día."),

    ficha_rutina(3, "Llegan visitas", "Antes de que suene el timbre",
        ["Cinco minutos de <b>contacto calmante</b> antes de que lleguen, si lo acepta.",
         "Asegúrate de que la <b>zona segura</b> está libre y accesible.",
         "Avisa a quien llega: <b>nada de saludarla, ni mirarla, ni agacharse</b> hacia ella al entrar.",
         "Que sea ella quien se acerque, cuando quiera. Si no se acerca, no pasa nada.",
         "Si se retira a su sitio, <b>ahí no se la toca</b>. Ni los niños."],
        clave="Invadir la distancia a la que un animal se siente seguro dispara ansiedad aunque no haya ningún peligro. Dejarle decidir la distancia es la mitad del trabajo."),

    ficha_rutina(4, "La visita al veterinario", "El día antes y el día de",
        ["El <b>transportín siempre fuera y abierto</b>, con una manta dentro, como un mueble más. No solo el día de la cita.",
         "Tira premios dentro durante los días previos, sin cerrar la puerta nunca.",
         "El día de: <b>cúbrelo con una toalla</b> para reducir estímulos durante el trayecto.",
         "En la sala de espera, <b>en alto y de cara a la pared</b>, no en el suelo ni frente a otros animales.",
         "Llévate premios de muchísimo valor y dáselos <b>durante</b> la exploración, no después."],
        clave="Si el transportín solo aparece el día de la consulta, se convierte en un predictor perfecto de miedo. Vaciarlo de significado es un trabajo de semanas, y dura años."),

    ficha_rutina(5, "Diez minutos de BÚSQUEDA", "Todos los días, o casi",
        ["Esparce una parte de su ración por la hierba, por una alfombra olfativa o entre toallas enrolladas.",
         "Déjala buscar <b>de tres a cinco minutos</b> sin interrumpir ni ayudar.",
         "Si es gato: comederos de juego, o la comida repartida y escondida por la casa.",
         "Hazlo <b>de forma preventiva</b>, no solo cuando ya está nerviosa.",
         "Y en el paseo, <b>diez minutos en los que elija ella</b> la ruta y huela sin prisa."],
        clave="Activar el sistema de BÚSQUEDA tiende a bajar la intensidad del miedo y del pánico. Un cerebro ocupado buscando sostiene peor una alarma al máximo volumen."),

    ficha_rutina(6, "Cuando ya está nerviosa", "En el momento, cuando ya ha empezado",
        ["<b>No intentes calmarla con palabras.</b> En plena alarma, el lenguaje llega mal.",
         "Saca el kit de búsqueda y <b>esparce comida</b> en el suelo, ahí mismo.",
         "O dale algo que masticar: masticar baja la activación.",
         "Si puedes, <b>aléjala del disparador</b> en vez de pedirle que lo tolere.",
         "Cuando se haya calmado, <b>no le pidas nada más</b> ese rato. Se acabó la sesión."],
        clave="Una vez que la alarma está al máximo, la capacidad de aprender se desploma. Pedirle cosas en ese estado no enseña nada y desgasta la confianza.",
        aviso="Si hay <b>autolesión</b>, pánico que no cede, o se hace daño intentando escapar: eso no es un mal momento, es una consulta. Y no esperes a la semana que viene."),

    cierre("Seis hojas, y el libro detrás", [
        "<b>La salida aburrida</b> y <b>la noche de ruido</b>, que son las dos que más veces se usan.",
        "<b>Las visitas</b> y <b>el veterinario</b>, que son las dos que más se improvisan y peor salen.",
        "<b>Los diez minutos de búsqueda</b>, que es lo único de esta carpeta que se hace todos los días.",
        "Y <b>qué hacer cuando ya ha empezado</b>, que es la que conviene tener leída antes de necesitarla.",
        "El porqué de todas ellas está en <b>Hogar en Calma</b>, capítulo a capítulo.",
    ]),
]

escribir("x1-rutinas-calma", "Rutinas de Calma", "#748156", "#E6EADA", RUT)


# ══════════════════════════════════════════════ 2 · NUTRICIÓN DORADA

NUT = [
    cubierta("Edad Dorada", "Alimentación",
             "Nutrición <em>Dorada</em>",
             "Qué hacer cuando comer se vuelve difícil: el apetito, el peso, la hidratación y lo que nunca debe entrar en su plato.",
             "Guía de alimentación senior"),

    pag('''  <div class="kicker">Lo primero de todo</div>
  <h1 class="ch-title">Lo que esta guía es, y lo que no</h1>
  <div class="ch-who">Léelo antes que nada: te ahorra un disgusto</div>

  <p class="lead">Esta guía <b>no es un recetario</b>, y no lo es a propósito.</p>

  <p>Una dieta casera que sustituya al alimento completo de tu mascota es, salvo que la formule un veterinario nutricionista, <b>una dieta desequilibrada</b>. Y en un animal mayor, con el riñón o el hígado trabajando peor, un desequilibrio sostenido hace daño de verdad. Hay recetarios por internet escritos por gente con muy buena intención que causan carencias serias.</p>

  <div class="box warn">
    <span class="lbl">La regla que no se negocia</span>
    <p>La base de su alimentación tiene que ser un <b>alimento completo y equilibrado</b>, y si hay enfermedad renal, hepática, cardíaca o diabetes, <b>una dieta prescrita por tu veterinario</b>. Todo lo que viene en estas páginas se suma a esa base: nunca la sustituye.</p>
  </div>

  <h3 class="sub"><span class="pre">Entonces para qué sirve</span>Lo que sí vas a encontrar</h3>
  <ul class="diamond">
    <li><b>Qué hacer cuando no come</b>, que es lo que más preocupa y lo que más se resuelve con un par de gestos.</li>
    <li><b>Los alimentos tóxicos</b>, en una página para pegar en la cocina.</li>
    <li><b>El peso</b>, que es la mayor palanca que tienes sobre el dolor articular.</li>
    <li><b>La hidratación</b>, que en gatos mayores es media batalla.</li>
    <li>Y <b>los premios</b>: cuáles, cuántos y cómo contarlos.</li>
  </ul>'''),

    pag('''  <div class="kicker">Para la cocina</div>
  <h1 class="ch-title">Lo que nunca debe comer</h1>
  <div class="ch-who">Imprime esta página y pégala donde se prepara la comida</div>

  <p class="lead">Esta es, de largo, la página más importante de la guía. No es una lista de «mejor evitar»: son alimentos que <b>intoxican</b>, y algunos matan.</p>

  <div class="signals">
    <div class="s"><span class="h">Chocolate y cacao</span><span class="d">cuanto más puro, más tóxico. El cacao en polvo es de lo peor.</span></div>
    <div class="s"><span class="h">Uvas y pasas</span><span class="d">pueden provocar fallo renal agudo, y no hay dosis segura conocida.</span></div>
    <div class="s"><span class="h">Cebolla, ajo, puerro y cebollino</span><span class="d">crudos, cocinados o en polvo. Destruyen glóbulos rojos.</span></div>
    <div class="s"><span class="h">Xilitol</span><span class="d">el edulcorante de chicles, caramelos «sin azúcar» y algunas cremas de cacahuete. Gravísimo en perros.</span></div>
    <div class="s"><span class="h">Alcohol y masa de pan cruda</span><span class="d">la masa sigue fermentando dentro del estómago.</span></div>
    <div class="s"><span class="h">Huesos cocinados</span><span class="d">se astillan. Perforan.</span></div>
    <div class="s"><span class="h">Aguacate, nueces de macadamia</span><span class="d">y frutos secos salados o con cáscara.</span></div>
    <div class="s"><span class="h">Café, té y bebidas con cafeína</span><span class="d">incluidas las latas energéticas.</span></div>
  </div>

  <div class="box warn">
    <span class="lbl">Y lo que casi nadie sabe</span>
    <p><b>Paracetamol e ibuprofeno matan gatos</b>, y en perros tampoco son analgésicos seguros. Nunca des un medicamento humano, ni el de otra mascota. Si sospechas que ha comido algo de esta lista: <b>llama ya a tu veterinario o a urgencias</b>, y no esperes a que aparezcan síntomas.</p>
  </div>'''),

    pag('''  <div class="kicker">El problema más frecuente</div>
  <h1 class="ch-title">Cuando no quiere comer</h1>
  <div class="ch-who">Primero por qué, y después qué hacer</div>

  <p class="lead">Con la edad bajan el olfato y el gusto, que son el motor del apetito. Pero antes de dar por hecho que es «que ya come menos», hay cuatro causas que se tratan.</p>

  <h3 class="sub" style="margin-top:5mm"><span class="pre">Lo que hay que descartar</span>Las cuatro causas tratables</h3>
  <ul class="diamond">
    <li><b>Dolor dental.</b> Mal aliento, babeo, come solo de un lado, prefiere lo blando. Es la causa más frecuente y la más ignorada.</li>
    <li><b>Náusea de fondo</b> por enfermedad renal, hepática o tumoral.</li>
    <li><b>Un medicamento</b> que haya empezado hace poco.</li>
    <li><b>Dolor al agacharse</b> hasta el comedero, si hay molestia cervical o de espalda.</li>
  </ul>

  <h3 class="sub"><span class="pre">Y lo que puedes hacer hoy</span>Seis gestos, por orden de eficacia</h3>
  <ul class="check">
    <li><b>Calienta la comida húmeda</b> un poco, hasta temperatura corporal. Potencia el olor y es lo que más funciona.</li>
    <li><b>Raciones pequeñas y frecuentes</b>, cuatro o cinco al día, en vez de dos grandes.</li>
    <li><b>Humedece el pienso</b> con agua templada o caldo sin sal, y déjalo ablandar diez minutos.</li>
    <li><b>Sube el comedero</b> si se agacha con esfuerzo.</li>
    <li><b>Come acompañada</b>, en sitio tranquilo y lejos del arenero si es gata.</li>
    <li><b>Pesa la comida</b> y anota lo que deja: es el único modo de saber si de verdad come menos.</li>
  </ul>

  <div class="box warn">
    <span class="lbl">Cuándo deja de poder esperar</span>
    <p><b>Más de 24 horas sin comer en un gato es urgencia veterinaria</b>, aunque parezca que está bien: el riesgo de lipidosis hepática es real y se revierte mal. En perros, más de 48 horas, o cualquier rechazo acompañado de vómitos, apatía o dolor.</p>
  </div>'''),

    pag('''  <div class="kicker">La mayor palanca</div>
  <h1 class="ch-title">El peso</h1>
  <div class="ch-who">Lo que más puedes hacer tú por sus articulaciones</div>

  <p class="lead">Si tu mascota tiene artrosis —y la gran mayoría de los senior tiene algún grado—, <b>el peso es lo que más puedes mover sin receta</b>. Cada kilo de más es carga sobre articulaciones que ya duelen.</p>

  <div class="box">
    <span class="lbl">La prueba de las costillas</span>
    <p>Pásale <b>la mano plana</b>, sin apretar, por el costado. Deberías notar las costillas como notas los nudillos del dorso de tu mano. Si tienes que hundir los dedos para encontrarlas, <b>le sobra peso</b>. Si se le marcan a la vista, le falta.</p>
    <p>Mírala también <b>desde arriba</b>: debe estrecharse en la cintura, por detrás de las costillas. Y <b>de perfil</b>: la barriga debe subir hacia la ingle, no ir recta.</p>
  </div>

  <h3 class="sub"><span class="pre">Cómo se baja</span>Despacio, y contando</h3>
  <ul class="check">
    <li><b>Pide a tu veterinario la ración exacta</b> para el peso objetivo. No la del paquete: la del animal que tienes delante.</li>
    <li><b>Pesa la comida</b> con báscula de cocina. A ojo nadie acierta.</li>
    <li><b>Cuenta los premios</b>: no deben pasar del <b>10 %</b> de lo que come al día, y lo que des en premios se descuenta de la ración.</li>
    <li><b>Pésala una vez al mes</b>, el mismo día, y anótalo en el diario.</li>
    <li>Nada de ayunos ni de bajadas rápidas: en gatos, perder peso deprisa es peligroso.</li>
  </ul>

  <h3 class="sub">Mi registro de peso</h3>
  <table class="fill">
    <thead><tr><th>Mes</th><th>Peso</th><th>Mes</th><th>Peso</th><th>Mes</th><th>Peso</th></tr></thead>
    <tbody><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody>
  </table>'''),

    pag('''  <div class="kicker">Media batalla en gatos</div>
  <h1 class="ch-title">El agua</h1>
  <div class="ch-who">Y los añadidos que sí puedes poner</div>

  <p class="lead">Un gato mayor bebe poco por diseño: viene de un animal de desierto que sacaba el agua de la presa. Con el riñón trabajando peor, eso se convierte en un problema.</p>

  <ul class="check">
    <li><b>Varios bebederos</b> repartidos por la casa, y <b>lejos del comedero</b>: un felino no bebe donde come.</li>
    <li><b>Cuencos anchos</b>, de cerámica o acero, donde los bigotes no rocen los bordes.</li>
    <li><b>Fuente de agua</b> en movimiento: muchos gatos beben bastante más.</li>
    <li><b>Comida húmeda</b> en parte de la ración: es la forma más fácil de que entre agua.</li>
    <li>Y <b>lejos del arenero</b>, siempre.</li>
  </ul>

  <div class="box">
    <span class="lbl">Añadidos seguros, y en qué cantidad</span>
    <p>Para hacer la comida más apetecible sin desequilibrar nada: <b>caldo de pollo o de pescado sin sal, sin cebolla y sin ajo</b> · un poco de agua del atún al natural · una cucharada de comida húmeda de su misma gama encima del pienso.</p>
    <p>Todo eso, sumado a los premios, <b>por debajo del 10 % de la ración diaria</b>. Por encima de ahí ya estás cambiando su dieta, no mejorándola.</p>
  </div>

  <div class="box warn">
    <span class="lbl">Si bebe mucho más de lo normal</span>
    <p>Un aumento marcado de sed y de orina <b>no es una curiosidad</b>: es uno de los primeros signos de enfermedad renal, diabetes e hipertiroidismo. Pide cita y dilo con esas palabras.</p>
  </div>'''),

    cierre("Lo que te llevas de esta guía", [
        "<b>La página de los alimentos tóxicos</b>, para la cocina. Es la que puede salvarle la vida.",
        "<b>Las cuatro causas tratables</b> de que no coma — empezando por el dolor dental, que es la más frecuente y la más ignorada.",
        "<b>La prueba de las costillas</b>, que te dice en diez segundos si le sobra peso.",
        "<b>La regla del 10 %</b> para los premios y los añadidos, que es lo que permite mimarla sin desequilibrar nada.",
        "Y la regla que sostiene todo lo demás: <b>la base es un alimento completo</b>, y si hay enfermedad, el que prescriba tu veterinario.",
    ]),
]

escribir("x2-nutricion-dorada", "Nutrición Dorada", "#A8502E", "#F6E9D6", NUT)


# ══════════════════════════════════════════════ 3 · 20 MOMENTOS

MOM = [
    cubierta("Edad Dorada", "Actividades",
             "20 <em>Momentos</em>",
             "Veinte cosas que podéis hacer juntas esta semana, pensadas para un cuerpo que ya no corre: de tres minutos a una tarde.",
             "Veinte tarjetas"),

    pag('''  <div class="kicker">Para qué son</div>
  <h1 class="ch-title">Veinte cosas que hacer juntas</h1>
  <div class="ch-who">Antes de que se acaben los días de hacerlas</div>

  <p class="lead">Un animal mayor sigue necesitando pasarlo bien. Lo que cambia no es la necesidad: <b>es la intensidad</b>. Donde antes había carreras, ahora hay olfato; donde había saltos, hay sol y mantas.</p>

  <p>Estas veinte tarjetas son actividades de <b>bajo impacto físico</b>, pensadas para un cuerpo que se cansa antes y al que puede dolerle algo. Ninguna pide correr, saltar ni forzar nada.</p>

  <div class="box">
    <span class="lbl">Cómo usarlas</span>
    <p><b>Una al día, o una a la semana.</b> No hay que hacerlas todas ni en orden. Elige la que encaje con el día que tienes y con el día que tiene ella.</p>
    <p>Y <b>hazle una foto</b> a los momentos que salgan bien. Esa es la mitad del sentido de esta carpeta: que dentro de unos años tengas algo más que la memoria.</p>
  </div>

  <div class="box warn">
    <span class="lbl">La regla de las veinte</span>
    <p><b>Si no le apetece, se acabó.</b> Ni insistir, ni sacarla de su sitio, ni «un poquito más». Una actividad que haya que imponer deja de ser un momento bueno y pasa a ser una exigencia — que es justo lo que no necesita.</p>
  </div>'''),

    pagina_momentos("Los sentidos", "Lo que mejor se conserva, y lo que más disfruta", [
        tarjeta(1, "La caja de los olores", "10 min",
                "Una caja de cartón con cosas de olores distintos: una hoja del parque, una prenda tuya, una bolsita de hierba, un trozo de corteza. Que la explore a su ritmo, sin pedirle nada.",
                "el olfato es lo último que se va, y es el sentido con el que más información recibe."),
        tarjeta(2, "El paseo de los diez minutos", "10 min",
                "Un tramo corto en el que <b>decide ella</b>: la ruta, el ritmo y cuánto rato huele cada cosa. No tiras de la correa ni una vez.",
                "poder decidir cosas pequeñas baja de forma medible el estrés basal."),
        tarjeta(3, "El baño de sol", "20 min",
                "Una manta en el sitio donde da el sol por la tarde, y tú al lado. Nada más. Si se duerme, mejor.",
                "el calor alivia la rigidez articular, y el sol ayuda a ordenar el ciclo de sueño, que en la vejez se desordena."),
        tarjeta(4, "Ventana con vistas", "libre",
                "Una cama o un cojín junto a una ventana por la que pase algo: gente, pájaros, hojas. En gatos, en alto.",
                "mirar es actividad mental sin coste físico — y en gatos, mirar desde arriba es su forma de sentirse a salvo."),
    ]),

    pagina_momentos("La mente", "Tres minutos valen más que media hora", [
        tarjeta(5, "El premio bajo el vaso", "3 min",
                "Tres vasos boca abajo y un premio debajo de uno, delante de ella. Que lo busque. Cuando acierte, se acaba.",
                "activa el sistema de BÚSQUEDA, que es el que mantiene despierta la motivación."),
        tarjeta(6, "La alfombra olfativa", "5 min",
                "Esparce parte de su ración en una alfombra olfativa, en una toalla enrollada o en la hierba. Sin ayudar.",
                "buscar la comida en vez de encontrarla servida es el enriquecimiento con mejor relación entre esfuerzo y beneficio."),
        tarjeta(7, "El truco de siempre", "3 min",
                "Pídele <b>algo que ya sepa hacer</b> y que no le cueste nada. Págalo muy bien. No le enseñes nada nuevo hoy.",
                "acertar algo fácil mantiene activos los circuitos de recompensa. Fallar algo difícil, no."),
        tarjeta(8, "La toalla con nudos", "5 min",
                "Una toalla vieja con dos o tres nudos flojos y un premio dentro de cada uno. Que la desate ella.",
                "manipular y resolver es un instinto que no se apaga con la edad: solo necesita una versión más suave."),
    ]),

    pagina_momentos("El cuerpo", "Contacto, no ejercicio", [
        tarjeta(9, "El masaje lento", "5 min",
                "Con ella tumbada, presión <b>suave y constante</b> con la palma abierta, de cuello a cola. Nada de palmaditas. Si se aparta, se acabó.",
                "el contacto sostenido y predecible activa el sistema de CUIDADO, que compite con el del miedo."),
        tarjeta(10, "El cepillado de la tarde", "10 min",
                "Cepillado suave, sobre todo en las zonas que ya no se alcanza. En gatos mayores, el lomo y la base de la cola.",
                "con la edad se asean menos, y el pelaje descuidado es una de las primeras señales de que algo duele."),
        tarjeta(11, "Las patas y las uñas", "5 min",
                "Un repaso de uñas y del pelo de entre las almohadillas, poco a poco y con premios. Una pata al día si hace falta.",
                "con las uñas largas apoya mal y resbala mucho más. Es de lo más barato que puedes hacer por su movilidad."),
        tarjeta(12, "Tres paseos cortos", "3 × 10 min",
                "Reparte el paseo largo en tres cortos, al ritmo que marque ella, por terreno llano y sin prisa.",
                "en un cuerpo con artrosis, el movimiento suave y repartido mantiene músculo; el esfuerzo largo lo castiga."),
    ]),

    pagina_momentos("El vínculo", "Lo que vas a recordar", [
        tarjeta(13, "Cinco minutos de nada", "5 min",
                "Siéntate a su altura, sin pedirle nada, sin móvil. Que decida ella si se acerca, si se aparta o si se queda.",
                "la presencia compartida sin exigencia es el único rato del día en que no se le pide nada a nadie."),
        tarjeta(14, "La sesión de fotos", "15 min",
                "Luz suave, a su altura, sin flash. Las patas, el hocico blanco, cómo duerme. <b>Y una con vosotras dos.</b>",
                "porque dentro de un tiempo vas a querer esas fotos, y ahora es cuando se pueden hacer."),
        tarjeta(15, "El sitio de siempre", "libre",
                "Volved a un sitio que le gustaba cuando era joven, aunque solo deis cuatro pasos y volváis en coche.",
                "reconocer un lugar conocido activa memoria y olfato a la vez, y suele animarlos visiblemente."),
        tarjeta(16, "La visita que le cae bien", "30 min",
                "Invita a la persona —o al animal— con quien siempre se ha llevado bien. Sesión corta y que se marche antes de que se canse.",
                "la inteligencia social se conserva mucho mejor que la memoria o el aprendizaje: sigue reconociendo y disfrutando."),
    ]),

    pagina_momentos("Celebrar", "Que la vejez también tenga días señalados", [
        tarjeta(17, "El cumpleaños", "una tarde",
                "Celébralo: su comida favorita dentro de la ración, un juguete nuevo, una foto. Aunque no sepas la fecha exacta, elige una.",
                "los rituales son para quien los hace. Marcar el año te ayuda a ti a verlo pasar y a no dejarlo pasar."),
        tarjeta(18, "El menú especial", "una comida",
                "Un añadido seguro sobre su comida de siempre: caldo sin sal, un poco de atún al natural, comida húmeda de su gama.",
                "con el olfato disminuido, un olor fuerte y agradable es una de las pocas cosas que todavía le despiertan ganas."),
        tarjeta(19, "La manta nueva", "libre",
                "Una manta o una cama nueva en su sitio de siempre, con una prenda tuya encima para que huela a ti desde el primer día.",
                "lo nuevo asusta menos cuando huele a conocido. Y una cama gruesa y firme le facilita levantarse."),
        tarjeta(20, "La lista de los días buenos", "5 min",
                "Escribe en el <i>Diario de los Días Buenos</i> lo mejor de esta semana. Una línea basta.",
                "cuando llegue una época difícil, la memoria se queda solo con lo malo. Esa página es la prueba de lo demás."),
    ]),

    pag('''  <div class="kicker">Para ir marcando</div>
  <h1 class="ch-title">Los veinte, y cuándo los hicimos</h1>
  <div class="ch-who">No hay que hacerlos todos. Pero da gusto verlos marcados</div>

  <table class="fill">
    <thead><tr><th>Nº</th><th>Momento</th><th>· Hecho</th><th>Fecha</th><th>Nº</th><th>Momento</th><th>· Hecho</th><th>Fecha</th></tr></thead>
    <tbody>''' + "".join(
        f'<tr><td class="day">{i:02d}</td><td></td><td class="box"></td><td></td>'
        f'<td class="day">{i+10:02d}</td><td></td><td class="box"></td><td></td></tr>'
        for i in range(1, 11)
    ) + '''</tbody>
  </table>'''),

    cierre("Veinte, y la regla de todas", [
        "<b>Los sentidos:</b> olfato, paseo propio, sol y ventana — lo que mejor se conserva.",
        "<b>La mente:</b> tres minutos valen más que media hora, y siempre terminando en un acierto fácil.",
        "<b>El cuerpo:</b> contacto y cuidado, no ejercicio. Masaje, cepillado, uñas y paseos repartidos.",
        "<b>El vínculo y la celebración:</b> las fotos, el sitio de siempre, el cumpleaños.",
        "Y la regla que va por encima de las veinte: <b>si no le apetece, se acabó.</b>",
    ]),
]

escribir("x3-20-momentos", "20 Momentos", "#A8502E", "#F6E9D6", MOM)


# ══════════════════════════════════════════════ 4 · CARTAS DE CONEXIÓN

CAR = [
    cubierta("Edad Dorada", "Escritura",
             "Cartas de <em>Conexión</em>",
             "Seis cartas para escribirle mientras está aquí, y para releer cuando ya no esté.",
             "Seis cartas"),

    pag('''  <div class="kicker">Antes de escribir</div>
  <h1 class="ch-title">Por qué escribirle</h1>
  <div class="ch-who">Sé que suena raro. Hazlo igual</div>

  <p class="lead">Escribirle una carta a un animal que no la va a leer parece absurdo. Y es, de todo lo que hay en este pack, <b>lo que más gente me ha dicho después que le cambió algo</b>.</p>

  <p>Hay dos motivos, y los dos son tuyos, no suyos.</p>

  <p><b>El primero:</b> poner palabras a lo que sientes baja su intensidad. Está estudiado — Matthew Lieberman lo demostró en 2007 con resonancia magnética: nombrar una emoción reduce la actividad de la amígdala. Escribir no es desahogarse por desahogarse: es neurología aplicada.</p>

  <p><b>El segundo es más sencillo y más importante:</b> escribir obliga a mirar. A acordarte de la primera vez, de las costumbres que tiene, de lo que te ha enseñado sin querer. Y mirar es justo lo que dejamos de hacer cuando llevamos años con alguien al lado.</p>

  <div class="box">
    <span class="lbl">Cómo hacerlo</span>
    <p><b>A mano, no a ordenador.</b> Escribir a mano es más lento, y esa lentitud es parte del ejercicio.</p>
    <p>Una carta cada vez, sin orden obligatorio. No hace falta que estén bien escritas: <b>nadie las va a leer</b> más que tú.</p>
    <p>Y cuando las termines, guárdalas juntas en algún sitio al que puedas volver.</p>
  </div>

  <div class="box warn">
    <span class="lbl">Y si hoy duele demasiado</span>
    <p>Déjalo. Estas cartas no tienen plazo, y escribirlas desde la angustia no sirve de nada. Vuelve otro día.</p>
  </div>'''),

    carta(1, "La primera vez",
          "Cuéntale cómo llegó. El día exacto si lo recuerdas, o lo que recuerdes: dónde estabas, qué pensaste al verla, qué pasó esa primera noche. Y si fue una decisión difícil, cuéntale también eso.", 11),

    carta(2, "Tus costumbres",
          "Las cosas que hace y que nadie más conoce: dónde se pone a dormir, qué hace cuando llegas, el ruido que hace antes de bostezar, lo que no soporta. Escríbelas ahora, porque son lo primero que se olvida.", 11),

    carta(3, "Lo que me enseñaste",
          "Sin ponerte solemne: qué sabes hoy por haber vivido con ella. Puede ser algo grande o puede ser aprender a esperar sin impacientarte. Las dos cosas cuentan.", 11),

    carta(4, "Lo que me habría gustado hacer distinto",
          "Esta es la que más cuesta, y la que más alivia. Lo que harías de otra forma, lo que no supiste a tiempo, el rato que dejaste pasar. Escríbelo y déjalo ahí. <b>No es para castigarte: es para dejar de darle vueltas a solas.</b>", 10),

    carta(5, "Tu día perfecto",
          "Descríbele un día entero hecho a su medida: por dónde pasearíais, qué comería, dónde dormiría la siesta, quién vendría a verla. Y luego mira la lista y <b>elige una cosa que puedas hacer esta semana</b>.", 10),

    carta(6, "Gracias",
          "La última. Sin estructura, sin preguntas y sin ayuda por mi parte. Lo que le quieras decir.", 12),

    autora('''  <p class="a-lead">Me llamo Victoria, tengo 44 años, y Tremdora existe por una perra que se llamaba Paris.</p>

  <p>Estuve <b>diecisiete años compitiendo con ella</b>, y durante todos esos años no escribí ni una línea sobre ella. Ni una.</p>

  <p>Lo que más me duele hoy no es haberla perdido: es <b>lo que no recuerdo</b>. El ruido exacto que hacía. Cómo se colocaba para dormir. La costumbre rarísima que tenía y que ahora no me sale. Todo eso lo tenía todos los días delante y pensé que no se olvidaba.</p>

  <p>Se olvida. Se olvida antes de lo que crees, y lo que queda después es una idea general, bonita y borrosa, donde antes había una perra concreta.</p>

  <p>Estas seis cartas son lo que me habría gustado tener escrito. Por eso insisto tanto en que las escribas <b>ahora</b>, mientras la tienes al lado y te parece que hay tiempo.</p>'''),

    cierre("Seis cartas, y lo que queda después", [
        "<b>La primera vez</b> y <b>tus costumbres</b>: lo concreto, que es exactamente lo primero que se borra.",
        "<b>Lo que me enseñaste</b>, que casi nunca es lo que uno espera al empezar a escribirlo.",
        "<b>Lo que habría hecho distinto</b>, que es la que más cuesta y la que más alivia — y que está escrita para dejar de darle vueltas a solas.",
        "<b>Tu día perfecto</b>, con una cosa de esa lista que puedes hacer esta misma semana.",
        "Y <b>gracias</b>, que es la única que no lleva instrucciones.",
    ]),
]

escribir("x4-cartas-conexion", "Cartas de Conexión", "#A8502E", "#F6E9D6", CAR)


# ══════════════════════════════════════════════ 5 · RITUAL DE 10 MINUTOS

RIT = [
    cubierta("Edad Dorada", "Rutina diaria",
             "Ritual de <em>10 Minutos</em>",
             "Diez minutos al día, siempre iguales y siempre a la misma hora: lo más barato y lo que más sostiene a una mascota mayor.",
             "Para hacer cada día"),

    pag('''  <div class="kicker">Por qué diez minutos</div>
  <h1 class="ch-title">La previsibilidad es el tratamiento</h1>
  <div class="ch-who">Y es gratis, y es aburrido, y es lo que más funciona</div>

  <p class="lead">Si de todo este pack solo pudieras hacer una cosa, haría esta. No porque sea la más impresionante, sino porque es <b>la única que se puede sostener todos los días</b> — y en un animal mayor, lo que se repite vale más que lo que se intenta.</p>

  <p>Con la edad, el cerebro pierde parte de su capacidad de regular las emociones: el mismo ruido de siempre puede generar hoy una reacción más intensa y más difícil de calmar. No es que se haya vuelto miedosa de carácter: es que <b>tiene menos reserva de frenos</b>.</p>

  <p>Y a la vez, el sistema del <b>CUIDADO</b> —el que se activa con el contacto afectuoso, la voz conocida y la rutina compartida— se mantiene fuerte, y suele convertirse en su ancla emocional principal. Eso explica por qué muchas mascotas mayores buscan <b>más</b> cercanía, no menos.</p>

  <div class="box">
    <span class="lbl">Lo que hace este ritual</span>
    <p>Activa ese sistema <b>a propósito y todos los días</b>, en lugar de dejarlo al azar de cómo venga la tarde. Un entorno que se puede anticipar reduce el miedo tanto como la ausencia de peligro real.</p>
  </div>

  <div class="box warn">
    <span class="lbl">La única regla</span>
    <p><b>La misma hora, el mismo sitio y la misma secuencia.</b> Si cambias el orden cada día, deja de ser un ritual y pasa a ser un rato agradable — que está bien, pero no es lo mismo y no hace lo mismo.</p>
  </div>'''),

    pag('''  <div class="kicker">El ritual</div>
  <h1 class="ch-title">Los cuatro tramos</h1>
  <div class="ch-who">Diez minutos, siempre en este orden</div>

  <div class="momento">
    <div class="mh"><span class="mn">1</span><span class="mt">El aviso</span><span class="md">30 segundos</span></div>
    <p class="mq">Siempre lo mismo: una palabra, un chasquido con la lengua, dar dos palmadas en la manta. Lo que sea, pero <b>idéntico cada día</b>.</p>
    <p class="mp"><b>Por qué:</b> es la señal que le dice que empieza. Al cabo de unas semanas, con oírla ya baja la activación — antes de que la toques.</p>
  </div>

  <div class="momento">
    <div class="mh"><span class="mn">2</span><span class="mt">El contacto</span><span class="md">4 minutos</span></div>
    <p class="mq">Con ella tumbada, <b>presión suave y constante</b> con la palma abierta, de cuello a cola. Nada de palmaditas ni de frotar. Respira tú despacio y audible mientras lo haces.</p>
    <p class="mp"><b>Por qué:</b> te está leyendo a ti también — tu ritmo respiratorio es información que usa. Y si en algún momento se aparta, se para: esto solo funciona si es voluntario.</p>
  </div>

  <div class="momento">
    <div class="mh"><span class="mn">3</span><span class="mt">La búsqueda</span><span class="md">3 minutos</span></div>
    <p class="mq">Un puñado de su ración esparcido en una alfombra olfativa, en una toalla o en la hierba. Que lo busque sola, sin ayuda y sin prisa.</p>
    <p class="mp"><b>Por qué:</b> activa el sistema de BÚSQUEDA sin coste físico. Es actividad mental para un cuerpo que ya no puede dar mucha actividad física.</p>
  </div>

  <div class="momento">
    <div class="mh"><span class="mn">4</span><span class="mt">El cierre</span><span class="md">2 minutos</span></div>
    <p class="mq">Vuelta a su sitio, una caricia lenta y <b>la misma palabra de siempre</b> para terminar. Y se acabó: no se alarga aunque vaya bien.</p>
    <p class="mp"><b>Por qué:</b> cerrar siempre igual es lo que convierte diez minutos sueltos en una rutina. Y terminar antes de que se canse hace que mañana lo espere.</p>
  </div>'''),

    pag('''  <div class="kicker">Variantes</div>
  <h1 class="ch-title">Si hoy no se puede</h1>
  <div class="ch-who">Tres versiones, para que ningún día se salte entero</div>

  <h3 class="sub" style="margin-top:0"><span class="pre">Versión gato</span>Lo mismo, pero sin invadir</h3>
  <p>El aviso igual. El contacto <b>solo si se acerca ella</b>: te sientas cerca y esperas, y si no viene, no pasa nada. La búsqueda, con comida repartida o en comedero de juego. Y el cierre, desde donde esté.</p>

  <h3 class="sub"><span class="pre">Versión día malo</span>Cuando le duele o está apagada</h3>
  <p>Solo <b>el aviso y el contacto</b>, y el contacto más corto y más suave. Nada de búsqueda. Que el ritual siga existiendo aunque hoy sea la mitad: lo que sostiene es que no falte, no que esté completo.</p>

  <h3 class="sub"><span class="pre">Versión tres minutos</span>Cuando la que no llega eres tú</h3>
  <p>Aviso, un minuto de contacto, un puñado de comida esparcida y el cierre. <b>Tres minutos hechos valen más que diez minutos pendientes.</b></p>

  <div class="box">
    <span class="lbl">Y si lo haces por la noche</span>
    <p>Hacerlo <b>antes de dormir</b> tiene una ventaja extra en mascotas mayores: muchos episodios de inquietud nocturna vienen de despertarse desorientados. Cerrar el día siempre igual ayuda a ordenar el ciclo de sueño, que es de lo primero que se desajusta.</p>
  </div>'''),

    pag('''  <div class="kicker">Para ir marcando</div>
  <h1 class="ch-title">Ocho semanas</h1>
  <div class="ch-who">Una casilla por día · completo, corto o nada</div>

  <table class="fill">
    <thead><tr><th>Sem.</th><th>· L</th><th>· M</th><th>· X</th><th>· J</th><th>· V</th><th>· S</th><th>· D</th><th>Cómo ha ido</th></tr></thead>
    <tbody>''' + "".join(
        f'<tr><td class="day">{i}</td>' + '<td class="box"></td>' * 7 + '<td></td></tr>'
        for i in range(1, 9)
    ) + '''</tbody>
  </table>

  <div class="box">
    <span class="lbl">Qué mirar a las ocho semanas</span>
    <p>No cuántas casillas hay marcadas. <b>Si espera el aviso.</b> Cuando un animal se coloca solo en su sitio al oír la señal, el ritual ya está hecho: a partir de ahí, los diez minutos se sostienen solos.</p>
  </div>

  <h3 class="sub">Lo que he notado</h3>
  ''' + lineas(3)),

    cierre("Diez minutos, cuatro tramos", [
        "<b>El aviso</b>, siempre el mismo, que acaba bajando la activación él solo.",
        "<b>El contacto</b>: presión suave y constante, y tu respiración lenta, que también la lee.",
        "<b>La búsqueda</b>: actividad mental para un cuerpo que ya no da actividad física.",
        "<b>El cierre</b>, que se hace igual aunque el día haya ido bien — y por eso mañana lo espera.",
        "Y las tres versiones, para que <b>ningún día se salte entero</b>: la de gato, la del día malo y la de tres minutos.",
    ]),
]

escribir("x5-ritual-10-minutos", "Ritual de 10 Minutos", "#A8502E", "#F6E9D6", RIT)
