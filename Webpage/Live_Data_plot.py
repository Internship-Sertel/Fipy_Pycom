import folium
import branca
import random
#import pandas as pd


def fancy_html():
    Latitude = random.randint(0,100)
    Longitude = 'Longitude'                          
    Date = 'Date'
    Time = 'Time'                                           
    Altitude ='Altitude'                               
    Speed = 'Speed'                            
    left_col_colour = "#2A799C"
    right_col_colour = "#C5DCE7"
    html = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="1" />
</head>
    <table style="height: 100px; width: 200px;">
<tbody>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Latitude</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(Latitude) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Longitude</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(Longitude) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Time</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(Time) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Altitude</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(Altitude) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Weather Conditions</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(Speed) + """
</tr>
</tbody>
</table>
</html>
"""
    return html
while 1:
    m = folium.Map(location = [12.9714, 80.24928],zoom_start = 15) 
    html = fancy_html()
    iframe = branca.element.IFrame(html=html,width=220,height=150)
    popup = folium.Popup(iframe,parse_html=True)
    folium.Marker([12.9714, 80.24928],popup=popup).add_to(m)
    m.save(" m.html ")
