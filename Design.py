import flet as ft
import datetime
from weather import forecast_details,weather_details

current_data = datetime.datetime.now()
formatted_date = current_data.strftime("%A,%B %d")
weather_data = weather_details('bangalore')
forecast_data = forecast_details('mumbai')

def main(page:ft.Page):
    page.title = "Weatherify"
    page.padding = 0
    page.vertical_alignment = "center"
    page.horizontal_alignment = 'center'
    page.window_width = 500
    page.window_height = 800
    page.theme = ft.theme.Theme(color_scheme_seed='green')
    page.window_bgcolor = "019877"
    
    page.fonts = {
        "Com-B":"./fonts/Comfortaa-Bold.ttf",
        "Com-L":"./fonts/Comfortaa-Light.ttf",
        "Com-M":"./fonts/Comfortaa-Medium.ttf",
        "Com-R":"./fonts/Comfortaa-Regular.ttf",
        "Com-SB":"./fonts/Comfortaa-SemiBold.ttf"
    }
    
    def hourly_items_report():
        items = []
        for k,v in forecast_data.items():
            time = k
            logo = v['logo']
            temp = v['temp_c']
            
            hourly_icon = ft.Image(height=50)
            hourly_time = ft.Text(font_family='Com-M',style='titleMedium',color=ft.colors.WHITE)
            hourly_temp = ft.Text(font_family='Com-M',style='titleLarge',color=ft.colors.WHITE)
            hourly_container = ft.Column([
                hourly_icon,
                hourly_time,
                hourly_temp
            ],horizontal_alignment='center',)
        
            hourly_icon.src = f"weather_icons/{logo}"
            hourly_temp.value = temp
            hourly_time.value = time
            items.append(
                ft.Container(
                    content=hourly_container,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    clip_behavior=ft.border_radius.all(5),
                    
                )
            )
        return items
            
    splash_screen_data = ft.Column([
        ft.Text(value="Weatherify",font_family="Com-B",style="displaySmall",text_align="center"),
        ft.Container(height=20),
        ft.Image(src="logo/logo.svg",width=200),
        ft.Container(height=20),
        ft.IconButton(
            icon=ft.icons.ARROW_FORWARD_IOS,
            icon_color=ft.colors.WHITE,
            icon_size=30,
            on_click=lambda _:page.go("/homepage")
        ),
        ft.Container(height=20),
        ft.Container(
            content=ft.Text(value=' Developer: Shridhar Kulkarni | ',
                            font_family="Com-M",style='labelLarge'),
            bgcolor="#019877",
            padding=10,
            border_radius=20
        )
    ],horizontal_alignment="center",alignment='center')
    
    splash_screen = ft.Container(
        content = splash_screen_data,
        gradient = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#001a131","#019877"]
        ),
        width=5000000,
        height=800,
        padding=20,
        border_radius=5
    )
    
    homepage_data = ft.Column([
        ft.Container(height=5),
        ft.Text(value=formatted_date,font_family="Com-L",color=ft.colors.WHITE,style="titleLarge"),
        ft.Text(value=weather_data['location'],font_family="Com-B",color=ft.colors.WHITE,style="titleLarge"),
        ft.Container(height=25),
        ft.Image(src=f"weather_icons/{weather_data['Icon']}",width=150),
        ft.Container(height=20),
        ft.Text(value=weather_data['condition'],font_family='Com-L',color=ft.colors.WHITE,
                style="titleLarge"),
        ft.Text(value=weather_data['temp_c'],font_family='Com-L',color=ft.colors.WHITE,
                style='displayLarge',size=100),
        ft.Container(height=25),
        ft.Divider(color=ft.colors.WHITE),
        ft.Row(spacing=10,controls=hourly_items_report(),scroll='auto'),
        ft.Row([
            ft.IconButton(
                icon=ft.icons.ARROW_BACK_IOS_NEW,
                icon_color= ft.colors.WHITE,
                icon_size=30,
                on_click= lambda _:page.go('/')
            ),
            ft.IconButton(
                icon=ft.icons.ARROW_FORWARD_IOS,
                icon_color=ft.colors.WHITE,
                icon_size=30,
                on_click=lambda _: page.go("/homepage/weatherdetails")
            )
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,)
    ],horizontal_alignment='center',alignment='center')
    
    homepage_body = ft.Container(
        content = homepage_data,
        gradient = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#001a131","#019877"]
        ),
        width=500,
        height=800,
        padding=20,
        border_radius=5
    )
    
    weather_indepth_data =ft.Column([
        ft.Container(height=5),
        ft.Text(value=formatted_date,font_family="Com-L",color=ft.colors.WHITE,style="titleLarge"),
        ft.Text(value=weather_data['location'],font_family="Com-B",color=ft.colors.WHITE,style="titleLarge"),
        ft.Container(height=15),
        ft.Divider(color=ft.colors.WHITE),
        ft.Container(height=5),
        ft.Row([
            ft.Text(value='Humidity',font_family='Com-L',color=ft.colors.WHITE,style='titleLarge'),
            ft.Text(value=weather_data['humidity'],font_family='Com-L',color=ft.colors.WHITE,style='titleLarge'),
            
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=5),
        ft.Row([
            ft.Text(value='Humidity',font_family='Com-L',color=ft.colors.WHITE,style='titleLarge'),
            ft.Text(value=weather_data['humidity'],font_family='Com-L',color=ft.colors.WHITE,style='titleLarge'),
            
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=5),
        ft.Row([
            ft.Text(value='Windspeed',font_family='Com-L',color=ft.colors.WHITE,style='titleLarge'),
            ft.Text(value=weather_data['windspeed'],font_family='Com-L',color=ft.colors.WHITE,style='titleLarge'),
            
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=5),
        ft.Row([
            ft.Text(value='Pressure',font_family='Com-L',color=ft.colors.WHITE,style='titleLarge'),
            ft.Text(value=weather_data['pressure'],font_family='Com-L',color=ft.colors.WHITE,style='titleLarge'),
            
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=5),
        ft.Row([
            ft.Text(value='Precipitation',font_family='Com-L',color=ft.colors.WHITE,style='titleLarge'),
            ft.Text(value=weather_data['precipitation'],font_family='Com-L',color=ft.colors.WHITE,style='titleLarge'),
            
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=5),
        ft.Row([
            ft.Text(value='UV Index',font_family='Com-L',color=ft.colors.WHITE,style='titleLarge'),
            ft.Text(value=weather_data['uv_index'],font_family='Com-L',color=ft.colors.WHITE,style='titleLarge'),
            
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=5),
        ft.Divider(color=ft.colors.WHITE),
        ft.Row(spacing=10,controls=hourly_items_report(),scroll='auto'),
        ft.Divider(color=ft.colors.WHITE),
        ft.IconButton(
                icon=ft.icons.ARROW_BACK_IOS_NEW,
                icon_color= ft.colors.WHITE,
                icon_size=30,
                on_click= lambda _:page.go('/homepage')
            ),
    ],horizontal_alignment='center',)
    
    
    weather_indepth_body = ft.Container(
        content = weather_indepth_data,
        gradient = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#001a131","#019877"]
        ),
        width=500,
        height=800,
        padding=20,
        border_radius=5
    )
    
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    splash_screen
                ],
                vertical_alignment="center",
                horizontal_alignment="center",
                padding=100,
                scroll="auto"
            )
        )
        
        if page.route == "/homepage" or page.route == "/homepage/weatherdetails":
            page.views.append(
                ft.View(
                    "/homepage",
                    [
                        homepage_body
                    ],
                    scroll="auto",
                    padding = 0,
                    vertical_alignment= "center",
                    horizontal_alignment="center"
                )
            )
            
        if page.route == "/homepage/weatherdetails":
            page.views.append(
                ft.View(
                    "/homepage/weatherdetails",
                    [
                        weather_indepth_body
                    ],
                    horizontal_alignment="center",
                    vertical_alignment="center",
                    scroll="always",
                    padding=60
                )
            )
        page.update()
        
    def view_top(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
        
    page.on_route_change = route_change
    page.on_view_pop = view_top
    page.go(page.route)

ft.app(target=main,assets_dir="assets")