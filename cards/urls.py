from django.urls import path

urlpatterns = [
    path('create-card/', views.create_card, name='create_card'),
    path('get-cards/', views.get_cards, name='get_cards'),
    path('get-card/<int:card_id>/', views.get_card, name='get_card'),
    path('update-card/<int:card_id>/', views.update_card, name='update_card'),
    path('delete-card/<int:card_id>/', views.delete_card, name='delete_card'),
]
