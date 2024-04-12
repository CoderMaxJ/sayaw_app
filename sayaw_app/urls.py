from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='reservation_App'
urlpatterns = [
  
    path('',views.mainpage, name='mainpage'),
    path('Add_new_guest/',views.add_guest ,name="add_guest"),
    path('Track_guest_records/', views.track_records, name="track_records"),
    path('Sayaw_rooms', views.view_rooms, name="rooms"),
    path('create_account/',views.create_account, name='create_account'),
    path('add_new_records/',views.add_new_records, name='add_new_records'),
    path('login-proces-authentication', views.login_process, name="login_process"),
    path('logout/', views.logout, name='logout'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('manage_Establishment/',views.manage_establisment_view,name='manage_establishment'),
    path('add_room/',views.add_room,name='add_room'),
    path('add_cottage/', views.add_cottage, name='add_cottage'),
    path('view_bookings/',views.view_bookings,name='view_bookings'),
    path('reservation_form/<int:id>',views.room_booking_view, name='room_booking_view'),
    path('cottage_reservationform/<int:id>',views.cottage_booking_view, name="cottage_booking"),
    path('processing_room_booking',views.room_booking_process, name="room_booking_process"),
    path('code_verification',views.transaction_code_checking, name='code_verification'),
    path('view_records/<int:id>',views.view_guest_records, name="view_records"),
    path('Reservation_Payment',views.pay, name='send_payment'),
    path('Payments_viewing/',views.payments_viewing, name="payments_viewing"),
    path('view_payment_proof/<int:id>',views.view_proof,name="view_payment_proof"),
    path('turn-paid',views.turn_paid, name='turn_paid'),
    path('Delete-record/<int:id>',views.delete_record, name='delete_record'),
    path('update-views/<int:id>', views.update_views ,name="update_view"),
    path('update-records/<int:id>', views.update_record, name="update_records"),
    path('cottage-booking-process/', views.cottage_booking_process , name="cottage_booking_process"),
    path('view-guest-records', views.guest_list ,name="guest_list"),
    path('confirmation/', views.confirmation, name="confirmation"),
    path('sayaw-cottage/<int:id>',views.view_sayaw_cottage, name="view_sayaw_cottage"),
    path('sayaw-rooms/<int:id>',views.view_photos, name='view_photos'),
    path('load-data', views.data_loading, name="data-loading"),
    path('chat-box,', views.chat, name="chat"),
    path('request-to-cancel', views.cancel_booking, name="cancel_booking"),
    path('cancel-booking-list', views.change_schedule , name="cancel-list"),
    path('cancellation-approval/', views.approve_cancellation, name="approve_cancellation"),
    path('add-nationality/', views.add_nationality, name="add-nationality"),
    path('refresher', views.refresher, name='refresher'),
    path('remove-services', views.remove_services , name="remove-services"),
    path('update-services/', views.update_services, name='update-services'),
    path('payment-approval-process/<int:id>', views.payment_effective, name="payment-effective"),
    path('update-bill/', views.down_payment, name='update-bill'),
    path('redirect-to-payments-viewing', views.goto_paidlist, name='goto_paidlist'),
    path('Feedback/<int:id>',views.feedback, name="send-feedback"),
    path('sending-message/', views.feedback_process, name="send-now"),
    path('phone-number-saving/', views.insert_number, name="insert"),
    path('Feedback-sent', views.clear_feedback, name="clear_feedback"),
    path('manage-account/', views.manage_account, name="manage_account"),
    path('set-availlable', views.reset, name="reset"),
    path('updating/', views.updating, name="updating"),
    path('code-tracking-process/', views.forgot_code, name="track-code"),
    path('collections', views.information_dashboard, name="information_dashboard"),
    path('guest-record-status-booking/',views.guest_dashboard, name="guest-dashboard"),
    path('change-Schedule/<int:id>',views.changeSchedule, name="changeschedule"),
    
    path('export-to-word/', views.export_to_word, name="export_to_word"),
   
    # path('Developer-security/', views.security, name="testing")
    
   
     
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
