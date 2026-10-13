import json
import folium
from folium.plugins import MarkerCluster
from folium import Element

# Cargamos los sitios de muestreo desde el archivo externo de forma limpia
with open("muestreos.json", "r", encoding="utf-8") as f:
    sitios_muestreo = json.load(f)

# Proveedor cartográfico libre de Esri (World Street Map)
url_esri = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}'
atribucion_esri = 'Tiles &copy; Esri'

mapa_rm = folium.Map(
    location=[-33.4372, -70.6506], 
    zoom_start=10, 
    tiles=url_esri, 
    attr=atribucion_esri
)

# FUNCIÓN JAVASCRIPT: Personaliza el clúster para mostrar el contenido al poner el cursor encima
funcion_hover_cluster = """
function(cluster) {
    var childCount = cluster.getChildCount();
    var markers = cluster.getAllChildMarkers();
    var titles = [];
    
    for (var i = 0; i < markers.length; i++) {
        // Recolectar los nombres guardados en el atributo "title" de cada marcador
        if (markers[i].options.title) {
            titles.push("• " + markers[i].options.title);
        }
    }
    
    // Unir los nombres con un salto de línea HTML (&#10;) para que se lean como lista
    var hoverText = titles.join('&#10;');
    
    var c = ' marker-cluster-';
    if (childCount < 10) { c += 'small'; }
    else if (childCount < 100) { c += 'medium'; }
    else { c += 'large'; }
    
    // Inyectamos hoverText en el atributo 'title' del div principal
    return new L.DivIcon({
        html: '<div title="' + hoverText + '"><span>' + childCount + '</span></div>',
        className: 'marker-cluster' + c,
        iconSize: new L.Point(40, 40)
    });
}
"""

# Aplicamos la función personalizada al crear el grupo de clústeres
cluster_muestreos = MarkerCluster(
    name="Sitios de Muestreo",
    icon_create_function=funcion_hover_cluster,
    options={'maxClusterRadius': 35,
             'spiderfyOnMaxZoom': True,  # Separa los puntos si están en el mismo sitio exacto al hacer zoom máximo
        'zoomToBoundsOnClick': True # HACE ZOOM AUTOMÁTICO AL APRETAR EL NÚMERO DEL CLÚSTER
        }
).add_to(mapa_rm)

# Añadir los marcadores AL CLÚSTER (no al mapa directamente)
for sitio, coords in sitios_muestreo.items():
    folium.Marker(
        location=coords,
        title=sitio,
        icon=folium.Icon(color="green", icon="leaf"),
        tooltip=folium.Tooltip(
            text=sitio, 
            permanent=True,
            direction="bottom", 
            opacity=0.85
        )
    ).add_to(cluster_muestreos)

# --- INYECCIÓN DEL BOTÓN Y REGLA CSS ---
# --- BOTÓN Y LÓGICA DE ZOOM / ETIQUETAS ---
script_interactivo = """
<div style="position: fixed; top: 15px; left: 55px; z-index: 9999;">
    <button id="btnEtiquetas" onclick="alternarEtiquetas()" style="background-color: #ffffff; border: 2px solid #28a745; border-radius: 5px; padding: 6px 12px; font-size: 14px; font-weight: bold; cursor: pointer; box-shadow: 2px 2px 5px rgba(0,0,0,0.3); color: #28a745; font-family: sans-serif;">
        Ocultar Etiquetas
    </button>
</div>

<style id="estilo-etiquetas"></style>

<script>
    var etiquetasVisibles = true;
    function alternarEtiquetas() {
        var btn = document.getElementById('btnEtiquetas');
        var styleSheet = document.getElementById('estilo-etiquetas');
        
        etiquetasVisibles = !etiquetasVisibles;
        
        if (!etiquetasVisibles) {
            styleSheet.innerHTML = '.leaflet-tooltip { display: none !important; }';
            btn.innerHTML = 'Mostrar Etiquetas';
            btn.style.color = '#6c757d';
            btn.style.borderColor = '#6c757d';
        } else {
            styleSheet.innerHTML = '';
            btn.innerHTML = 'Ocultar Etiquetas';
            btn.style.color = '#28a745';
            btn.style.borderColor = '#28a745';
        }
    }
</script>
"""

mapa_rm.get_root().html.add_child(Element(script_interactivo))
# -----------------------------------------------

mapa_rm.save("mapa_sitios_muestreo.html")
print("Mapa actualizado con zoom automático en clústeres.")