
import 'package:flutter/material.dart';
import 'package:patrolling_robot/src/Home/home_screen.dart';
import 'package:patrolling_robot/src/Network/network.dart';
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
      initialRoute: '/',
      routes: {
        '/': (context) => const HomeScreen(),
        VideoStream.route: (context) => const VideoStream(),
        Network.route: (context) => const Network()
      },
    ); 
  }
}
