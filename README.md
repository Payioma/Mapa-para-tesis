# Mapa de Sitios de Muestreo - Tesis de Ingeniería Agrónoma

Repositorio de código y recursos cartográficos para el Trabajo Final de Título titulado: *"Riqueza de parasitoides de pseudocóccidos (Hemiptera: Coccoidea) en la Región Metropolitana"* (Paloma Paredes, Universidad Mayor, 2026).

---

## 📌 Descripción del Proyecto
Este proyecto contiene scripts en Python automatizados con la librería `folium` para generar un mapa interactivo de la Región Metropolitana de Chile. El mapa visualiza la distribución geográfica de los sitios de muestreo (comunas como Vitacura, Lampa, Huechuraba y Quinta Normal), asociando cada punto a su respectivo hospedero vegetal y facilitando la validación espacial de los insectos benéficos evaluados en el estudio.

---

## 🗂️ Estructura del Repositorio

```text
├── cuadreno.py                 # Script principal en Python para la generación del mapa interactivo
├── muestreos.json              # Archivo de datos externo con las coordenadas y descripciones de los sitios
├── mapa_sitios_muestreo.html   # Archivo HTML final generado (mapa interactivo con clústeres y controles)
└── README.md                   # Documentación oficial del proyecto
```

---

## 🚀 Requisitos e Instalación

Para ejecutar y modificar este script en tu entorno local o en la nube (como GitHub Codespaces), asegúrate de tener instalado Python junto con la librería de cartografía `folium`.

1. Instala las dependencias necesarias ejecutando el siguiente comando en tu terminal:
   ```bash
   pip install folium
   ```

---

## 💻 Uso e Instrucciones de Ejecución

1. **Verificar los datos:** Asegúrate de que el archivo `muestreos.json` contenga las coordenadas y etiquetas actualizadas de cada sitio de muestreo.
2. **Ejecutar el script principal:**
   ```bash
   python cuadreno.py
   ```
3. **Visualizar el mapa:** El script sobrescribirá o generará un archivo llamado `mapa_sitios_muestreo.html`. Abre este archivo haciendo doble clic sobre él en tu explorador de archivos para visualizarlo en cualquier navegador web. En caso de no abrir, descarga el archivo html y abrelo desde la carpeta de descargas.

---

## ⚙️ Características Técnicas del Mapa
* **Cartografía Base:** Utiliza mosaicos vectoriales libres de *Esri (World Street Map)*, optimizados para evitar bloqueos por restricciones de claves de API (*API Keys*).
* **Agrupación Inteligente (MarkerCluster):** Agrupa automáticamente las comunas vecinas en vistas panorámicas y las separa dinámicamente al aplicar zoom.
* **Control de Etiquetas:** Incluye un botón flotante personalizado para alternar la visibilidad de las etiquetas de los hospederos vegetales de forma global.