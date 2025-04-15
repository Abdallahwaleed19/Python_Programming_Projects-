// void main() {
//   int age = 20;
//   String name = "Abdallah";
//   print("The Player name is : $name and he is age is : $age");
// }

// void main (){
//   for (int i = 0; i < 10; i++) {
//     print(i);
//   }
// }

// class Car {
//   String? brand;
//   String? model;
//   double? price;
//   Car(this.brand, this.model, this.price);
//   void display() {
//     print("$brand , $model , $price");
//   }
// }

// void main() {
//   Car car1 = Car("BMW", "X5", 50000);
//   car1.display();
// }

// void task1() {
//   print("Task 1 done");
// }

// void task2() {
//   print("task 2 done");
// }

// void main() {
//   task1();
//   task2();
// }

// Future<void> task1() async {
//  await Future.delayed(Duration(seconds: 2));
//  print("Task 1 done");
// }
// void task2() {
//   print("task 2 done");
// }
// void main() async {
//   await task1();
//   task2();
// }

// mixin fly {
//   void flying() {
//     print("Flying");
//   }
// }
// class Bird with fly {
//   @override
//   void flying() {
//     print("Flying");
//   }
// }
// void main() {
//   Bird bird = Bird();
//   bird.flying();
// }

// class Animal {
//   void sound () {
//     print("Animal sound");
//   }
// }
// class Dog extends Animal {
//   @override
//   void sound() {
//     print("HAOHAO");
//   }
// }
// void main() {
//   Dog dog1 = Dog();
//   dog1.sound();
// }

// abstract class Shape {
//   void area();
//   void perimeter();
// }
// class Circle extends Shape {
//   double radius;
//   Circle(this.radius);
//   @override
//   void area() {
//     double area = 3.14 * radius * radius;
//     print("The area of the circle is: $area");
//   }
//   @override
//   void perimeter() {
//     double perimeter = 2 * 3.14 * radius;
//     print("The perimeter of the circle is: $perimeter");
//   }
// }
// void main() {
//   Circle circle = Circle(5);
//   circle.area();
//   circle.perimeter();
// }

// class Animal {
//   void sound() {
//     print("Animal sound");
//   }
// }

// class Dog implements Animal {
//   @override
//   void sound() {
//     print("HAOHAO");
//   }
// }

// class Cat implements Animal {
//   @override
//   void sound() {
//     print("Meow");
//   }
// }
// void main() {
//   Dog dog = Dog();
//   Cat cat = Cat();
//   dog.sound();
//   cat.sound();
// }

// import 'dart:isolate';

// void factorial(SendPort sendport) {
//   int result = 1;
//   int fact = 5;
//   for (int i = 1; i <= fact; i++) {
//     result *= i;
//   }
//   sendport.send(result);
// }

// void main() async {
//   ReceivePort receiveport = ReceivePort();
//   await Isolate.spawn(factorial, receiveport.sendPort);
//   receiveport.listen((message) {
//     print("The Factorial Result is : $message");
//   },);
// }


// import 'dart:isolate';
// void sumList(List<dynamic> args) {
//  SendPort sendPort = args[0];
//  List<int> numbers = args[1];
//  int sum = numbers.reduce((a, b) => a + b);
//  sendPort.send(sum);
// }
// void main() async {
//  ReceivePort receivePort = ReceivePort();
//  List<int> numbers = [1, 2, 3, 4, 5];
//  await Isolate.spawn(sumList, [receivePort.sendPort, numbers]);
//  receivePort.listen((result) {
//  print('Sum: $result'); 
//  });
// }
