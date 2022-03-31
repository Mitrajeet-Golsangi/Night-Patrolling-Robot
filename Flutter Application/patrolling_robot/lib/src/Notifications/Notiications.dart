import 'package:flutter_local_notifications/flutter_local_notifications.dart';

class NotificationsAPI {
  static const AndroidInitializationSettings _androidInitializationSettings =
      AndroidInitializationSettings('flutter_logo');

  static const initializationSettings =
      InitializationSettings(android: _androidInitializationSettings);
  static final _notifications = FlutterLocalNotificationsPlugin();

  static Future<NotificationDetails> _notificationDetails() async {
    await _notifications.initialize(initializationSettings);
    return const NotificationDetails(
      android: AndroidNotificationDetails('notificationsChannel', 'Security',
          channelDescription:
              'Notification is received if the robot detects a face in the vicinity',
          importance: Importance.max,
          channelShowBadge: true,
          playSound: true),
      // iOS: IOSNotificationDetails(),
    );
  }

  static Future notify(
      {int id = 0, String? title, String? body, String? payload}) async {
    _notifications.show(id, title, body, await _notificationDetails(),
        payload: payload);
  }
}
