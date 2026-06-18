---
title: "Autito de máxima distancia a capacitor"
autor: "José Juarez"
version: "14/06/26"
---


<!-- Image -->
<br>
   <center>![](){width=400px}</center>
   <center>
      <span class="grey3 size70">. </span>
      <span class="grey3 size50">Fuente: </span>
   </center>
<br>



<!-- *** GUIDE START *** -->

(ofertas en ML salvo aclaración)

### Electrónica

- Es bueno poner una resistencia de carga para que la corriente de carga no suba demasiado
- Supercapacitor (1F, 5F, 10F, etc.)

  + Capacitor 10 F 2.7v Back Up Radial 30x10mm Supercapacitor $7665
- Resistencia para regular la descarga: consume energía $P = I^2 \cdot R$

##### Resistencia para regular la descarga

Una descarga más lenta podría mejorar la eficiencia global del sistema en algunos casos. Por ejemplo, si el motor consume corrientes muy altas al arrancar, puede haber pérdidas importantes en el bobinado. Sin embargo, en un proyecto escolar sencillo, es muy poco probable que una resistencia serie compense la energía que ella misma desperdicia.

Yo lo plantearía como una hipótesis para que los alumnos la comprueben: "¿Agregar una resistencia hará que el auto llegue más lejos?" Muchos pensarán que sí porque "gasta más despacio". Luego pueden medir y descubrir que la resistencia también consume energía.

Un ejemplo extremo ayuda a verlo:

Sin resistencia, el motor recibe mucha corriente, acelera rápido y el auto sale disparado.
Si gran parte de esa energía se pierde en patinamiento de ruedas, golpes, vibraciones o corrientes muy altas en el motor, una descarga más suave podría resultar más eficiente.

En cambio:

Si el auto ya está bien diseñado y las ruedas no patinan, agregar una resistencia probablemente solo quite energía útil y reduzca la distancia.

De hecho, en muchos vehículos eléctricos reales se controla la potencia para evitar corrientes excesivas, pero no mediante una resistencia, sino con electrónica de conmutación (PWM), precisamente para no desperdiciar energía en calor.


---


### Chasis

##### Materiales posibles:

- Chapa de acero fina (0,5 a 0,8 mm) plegada en U o C. Uniones de remache, también puede funcionar el estaño. Si tienes chapa de acero de latas de conserva (no de aluminio), el estaño sí funciona bastante bien con fundente adecuado.

- Perfiles de aluminio unidos por remaches pop de 2,4 mm o remaches macizos o remaches hechos con alambre de aluminio

- Remaches:

   + Remache Pop Rerar 2,4 X 6 Pack X 200 Unidades $10.708, x 100 unidades $6.631
   + Remache De Aluminio Macizos 2,3 X 3 mm. x 100 unidades $15.225

- Perfiles de aluminio más adhesivo epoxi (peligro con las manos y ojos de los chicos)


---


### Motor

- Motor DC tipo 130 (130 se refiere al tamaño normalizado, no a la potencia, tensión o velocidad)

  + Motor Dc 16500 Rpm 3v A 6v Modelo 130 Para Caja Recutora. $3510 (tiene las dimensiones la publicación)

---


### Transmisión

- Polea motor: 5mm, polea eje: 20 a 30 mm



---


### Posibles variantes del proyecto

##### Diseño común solo experimentan la electrónica

- Parte común (la entregas tú)

  - Chasis.
  - Motor.
  - Ejes y ruedas.
  - Capacitor.
  - Pista de ensayo.

- Parte de diseño de los alumnos

  - Circuito de descarga.
  - Valor de la resistencia (o ausencia de resistencia).
  - Relación de transmisión mediante distintas poleas.
  - Estrategia de carga.

###### Hipótesis y mediciones.

Así la competencia pasa a ser realmente un problema de ingeniería: ¿Conviene una descarga rápida o lenta para maximizar la distancia? Y la respuesta no es obvia. Además, desde el punto de vista didáctico, me gusta que la resistencia tenga posibilidades de "ganar" o "perder". Si el resultado fuera evidentemente peor, no habría mucho para investigar. En cambio aquí los alumnos pueden argumentar cosas razonables en ambos sentidos:

  - "Sin resistencia aprovecho toda la energía."
  - "Con resistencia el motor funciona más tiempo."

Luego hacen el experimento y comparan.

Incluso podrías pedirles antes de construir:

- Formular una hipótesis.
- Justificarla.
- Construir.
- Medir distancia.
- Explicar diferencias entre predicción y resultado.


##### Diseño del chasis libre

Si todos usan el mismo motor y el mismo capacitor, una parte importante del resultado dependerá del peso del vehículo. Eso puede convertir el diseño del chasis en un problema de ingeniería auténtico: ¿Conviene una estructura muy liviana pero flexible, o una más rígida pero pesada? Esa pregunta no tiene una respuesta obvia y puede generar diseños muy distintos entre grupos. Para una materia de diseño y mecanizado, me parece incluso más interesante que la parte electrónica.




<!-- *** GUIDE END *** -->


<!-- *** GUIDE AUXILIARY TEMPLATES *** -->


<div hidden>


<!-- Learning objectives very briefly -->
<span class="grey3 size85">.</span>

<!-- Image -->
<br>
   <center>![](){width=400px}</center>
   <center>
      <span class="grey3 size70">. </span>
      <span class="grey3 size50">Fuente: </span>
   </center>
<br>

<!-- Videos: change XXX to the video-id and put time (seconds) -->
<!-- Yotube with start point -->
👉 [Mira este momento clave en el video](https://www.youtube.com/watch?v=XXX&t=123s)
🎬 [Un fragmento que vale la pena ver](https://www.youtube.com/watch?v=XXX&t=123s)
🔎 [Este detalle del video te va a interesar](https://www.youtube.com/watch?v=XXX&t=123s)
⚡ [Dale play a esta parte y fijate qué pasa](https://www.youtube.com/watch?v=XXX&t=123s)
<!-- Youtubetrimmer with start and end point -->
👉 [Mirá este momento puntual del video](https://youtubetrimmer.com/view/?v=XXX&start=120&end=150&loop=0)
🎬 [Este fragmento explica justo lo que necesitamos](https://youtubetrimmer.com/view/?v=XXX&start=120&end=150&loop=0)
⚡ [Dale play a esta parte y sacá tus conclusiones](https://youtubetrimmer.com/view/?v=XXX&start=120&end=150&loop=0)
🔎 [Fijate qué pasa en este momento](https://youtubetrimmer.com/view/?v=XXX&start=120&end=150&loop=0)

<!-- Visible story or anecdote -->
<span class="grey3 size85">...</span>

<!-- Sections -->
<br><span class="grey3 size70">🔁 Repaso:</span>
<br><span class="grey3 size70">🛠️ Trabajo:</span>
<br><span class="grey3 size70">📘 Teoría:</span>
<br><span class="grey3 size70">✅ Autoevaluación:</span>
<br><span class="grey3 size70">📝 Práctica:</span>
**1.**  **:**
**2.** **:** 

<!-- Solutions -->
<div class="grey3 size70">.</div>


</div>


<!-- Guide style definitions -->
<style>
/* Colors */
.grey1 {color: #b3b3b3;} /* my light-grey */
.grey2 {color: #999999;} /* my middle-grey */
.grey3 {color: #808080;} /* my dark-grey */
.blue1 {color: #6495ed;} /* nvim blue */
.blue2 {color: #276cdf;} /* Andrew Ng Blue */
.sky1 {color: #7dbed8;} /* nvim sky */
.sky2 {color: #27a2db;}   /* my sky */
.green {color: #81b524;} /* my green */
.red1 {color: #ec5469;} /* my coral-red */
.red2 {color: #f44336;} /* my red */
.rose {color: #ec9998:} /* nvim rose */
.gold {color: #df9d43;} /* Andrew Ng gold */
.orange1 {color: #fda556;} /* nvim orange */
.orange2 {color: #ff9505;} /* Andrew Ng orange */
.purple1 {color: #ff40ff;} /* Andrew Ng purple */
.purple2 {color: #d164d7;} /* Andrew Ng purple */
/* Font Size */
.size90 {font-size: 0.9em;}
.size85 {font-size: 0.85em;}
.size80 {font-size: 0.8em;}
.size70 {font-size: 0.7em;}
.size60 {font-size: 0.6em;}
.size50 {font-size: 0.5em;}
/* Document General Font Size */
body {font-size: 1.3em;}
/* Bullet "1." see as "1)" */
ol {list-style-type: decimal;}
ol li::marker {content: counter(list-item) ") ";}
/* Two columns */
.two-columns {
  column-count: 2; /* Number of columns */
  column-gap: 20px;
}
/* Indent the example */
.example {margin-left: 20px;}

/* =========================
   IMPRESIÓN A4 – GUÍAS
   ========================= */
@media print {

  @page {
    size: A4;
    margin: 1.2cm;
  }

  body {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 10.5pt;
    line-height: 1.35;
    color: #000;

    column-fill: auto; /* Llena una columna y después la otra*/
    column-count: 2;
    column-gap: 1cm;
  }

  h1 {
    font-size: 14pt;
    margin: 0 0 6pt 0;
  }

  h2 {
    font-size: 12pt;
    margin: 8pt 0 4pt 0;
  }

  h3 {
    font-size: 11pt;
    margin: 6pt 0 3pt 0;
  }

  h1, h2, h3 {
    break-after: avoid;
    break-inside: avoid;
  }

  p {
    margin: 0 0 4pt 0;
    text-align: justify;
    break-inside: avoid;
  }

  ul, ol {
    margin: 0 0 4pt 12pt;
    padding: 0;
  }

  li {
    margin-bottom: 2pt;
  }

  code, pre {
    font-family: "Courier New", Courier, monospace;
    font-size: 9.5pt;
    background: #f2f2f2;
    padding: 1px 3px;
    border-radius: 2px;
  }

  pre {
    padding: 6pt;
    overflow: hidden;
    break-inside: avoid;
  }

  img {
    max-width: 100%;
    height: auto;
    break-inside: avoid;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 9.5pt;
  }

  th, td {
    border: 1px solid #000;
    padding: 3pt;
  }

  nav, footer, .no-print {
    display: none;
  }
}
</style>
<!-- Remember: Use <span> inline and <div> with several lines --->
