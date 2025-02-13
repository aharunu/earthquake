import pydeck as pdk

from app.api.get_earthquake import get_earthquake

def get_three_d_map():
    data = get_earthquake(90)

    # Define a layer to display on a map
    layer = pdk.Layer(
        "HexagonLayer",
        data,
        get_position=["longitude", "latitude"],
        auto_highlight=True,
        elevation_scale=50,
        pickable=True,
        elevation_range=[0, 3000],
        extruded=True,
        coverage=1,
    )

    average_longitude = data["longitude"].mean()
    average_latitude = data["latitude"].mean()

    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=average_longitude,
        latitude=average_latitude,
        zoom=4,
        min_zoom=1,
        max_zoom=20,
        pitch=40.5,
        bearing=-27.36,

    )

    # Render
    r = pdk.Deck(layers=[layer], initial_view_state=view_state)
    return r._repr_html_()
    
