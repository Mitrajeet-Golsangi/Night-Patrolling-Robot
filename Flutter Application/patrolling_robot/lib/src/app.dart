
import 'package:flutter/material.dart';
import 'package:patrolling_robot/src/VideoStream/VideoStreaming.dart';

class MainPage extends StatefulWidget {
  const MainPage({Key? key}) : super(key: key);

  @override
  State<MainPage> createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      darkTheme: ThemeData(brightness: Brightness.dark),
      themeMode: ThemeMode.dark,
        home: const VideoStream()
        // home: Scaffold(
        //   body: Center(
        //       child: ElevatedButton(
        //     child: const Text("Notification !"),
        //     onPressed: ()   => NotificationsAPI.notify(
        //         title: "Notification !",
        //         body: "This is a custom test notification and this is "
        //             "a really long body."),
        //   )),
        // )
    );
  }
}
