from admin_tools.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):


    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)


        self.children.append(
            modules.ModelList(
                title=u'Пользователи',
                models=(
                    'django.contrib.auth.*',
                ),
            )
        )

        self.children.append(modules.Group(
            title=u"Статистика",
            display="tabs",
            children=[

                modules.ModelList(
                    title=u'Товары',
                    models=(
                        'shop.models.*',
                    ),
                ),

                modules.ModelList(
                    title=u'Заказы',
                    models=(
                        'orders.models.*',
                    ),
                ),
            ]
        ))

        self.children.append((modules.Group(
            title=u"Товары",
            display="tabs",
            children=[

                modules.ModelList(
                    title=u"Категории",
                    models=(
                        'shop.models.category',
                    )
                ),

            ]
        )
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            title='Последние действия',
            limit=15
        ))





