// void main() {
//   for (int i = 1; i <= 10; i++) {
//     if (i == 5) {
//       break;
//     }
//     print(i);
//   }
// }

// void main() {
//   for (int i = 1; i <= 10; i++) {
//     if (i == 5) {
//       continue;
//     }
//     print(i);
//   }
// }

// void main() {
//   int num1 = 15;
//   int num2 = 8;
//   int sum = num1 + num2;
//   int difference  = num1 - num2;
//   print (sum);
//   print (difference);
// }

// void main() {
//   List<String> names = ["Alice", "Bob", "Charlie"];
//   names.add("David");
//   print(names);
// }

// void main() {
//   Map<String, int> map = {"Eve": 25, "Frank": 30, "Grace": 22};
//   print(map);
//

// double calculateArea (int radius){
//   var area = 3.14 * radius * radius;
//   return area;
// }
// void main(){
//   double area = calculateArea(5);
//   print(area);
// }

// import 'dart:io';

// void main() {
//   stdout.write("Enter a number: ");
//   int num = int.parse(stdin.readLineSync()!);
//   if (num > 0) {
//     print("Postive");
//   }
//   else if (num < 0) {
//     print("Negative");
//   }
//   else {
//     print("Zero");
//   }
// }

// void main() {
//   int day = 4;
//   switch (day) {
//     case 1:
//       print("STR");
//       break;
//     case 2:
//       print("SUN");
//       break;
//     case 3:
//       print("MON");
//       break;
//     case 4:
//       print("THU");
//       break;
//     case 5:
//       print("WED");
//       break;
//     case 6:
//       print("THR");
//       break;
//     case 7:
//       print("FRI");
//       break;
//     default:
//       print("Error Input");
//   }
// }

// void main() {
//   int sum = 0;
//   for (int i = 0; i <= 100; i++) {
//     sum += i;
//   }
//   print(sum);
// }

// void main() {
//   for (int i = 20; i <= 40; i++) {
//     while (i % 2 == 0) {
//       print(i);
//       i++;
//     }
//   }
// }

// void main() {
//    int counter = 1;
//   do {
//     print(counter);
//     counter++;
//   } while (counter <= 5);
// }

// void main() {
//   List<int> numbers = [10, 20, 30, 40, 50, 60];
//   for (int number in numbers) {
//     if (number == 50) {
//       print("found number");
//       break;
//     }
//   }
// }

// void main(){
//   List<int> numbers = [10, 20, 31, 45, 50, 60];
//   for (int number in numbers) {
//     if (number % 2 !=0) {
//       continue;
//     }
//     print(number);
//   }

// }

// void greet(String name) {
//   print("Hello $name");
// }

// void main() {
//   greet("Abdallah");
// }

// void add(int num1, int num2) {
//   int sum = num1 + num2;
//   print(sum);
// }

// void main() {
//   add(5, 5);
// }

// void describePerson({required String name, int age = 0}) {
//   print("Name: $name, Age: $age");
// }
// void main() {
//   describePerson(name: "Abdallah", age: 20);
// }

// class Dog {
//   String? name;
//   int? age;
//   String? breed;
//   void displayInfo(){
//     print("Name: $name, Age: $age, Breed: $breed");
//   }
// }
// void main() {
//   Dog dog1 = Dog();
//   dog1.name = "Buddy";
//   dog1.age = 3;
//   dog1.breed = "Golden Retriever";
//   dog1.displayInfo();
// }

// class Dog {
//   String? name;
//   int? age ;
//   String? breed ;
//   Dog(this.name , this.age , this.breed);
// }
// void main() {
//   Dog dog1 = Dog("Buddy", 3, "Golden Retriever");
//   print("Name: ${dog1.name}, Age: ${dog1.age}, Breed: ${dog1.breed}");
// }

// class Dog {
//   String? name;
//   int? age ;
//   String? breed ;

//   Dog(this.name , this.age , this.breed);

//   Dog.namedConstructor(String name) : this(name, 0, "Unknown");
// }
// void main() {
//   Dog dog1 = Dog.namedConstructor("Buddy");
//   print("Name: ${dog1.name}, Age: ${dog1.age}, Breed: ${dog1.breed}");
// }

// class BankAccount {
//   double _balance;

//   BankAccount(this._balance);

//   void deposit(double amount) {
//     if (amount < 0) {
//       throw ArgumentError('Deposit amount cannot be negative');
//     }
//     _balance += amount;
//   }

//   void withdraw(double amount) {
//     if (amount < 0) {
//       throw ArgumentError('Withdrawal amount cannot be negative');
//     }
//     if (amount > _balance) {
//       throw ArgumentError('Insufficient funds');
//     }
//     _balance -= amount;
//   }

//   double get balance => _balance;

//   set balance(double value) {
//     if (value < 0) {
//       throw ArgumentError('Balance cannot be negative');
//     }
//     _balance = value;
//   }
// }

// void main() {
//   BankAccount account = BankAccount(1000);
//   account.deposit(500);
//   account.withdraw(200);
//   print(account.balance);
// }

// class Vehicle {
//   String? brand;
//   String? model;
// }

// class Car extends Vehicle {
//   int? numberofdoors;
// }
// void main() {
//   Car car = Car();
//   car.brand = "BMW";
//   car.model = "X5";
//   car.numberofdoors = 4;
//   print(car.brand);
//   print(car.model);
//   print(car.numberofdoors);
// }

// class Shape {
//   double area() {
//     return 0; // default area
//   }
// }

// class Rectangle extends Shape {
//   int length;
//   int width;
//   Rectangle(this.length, this.width);
//   @override
//   double area() {
//     return length * width.toDouble(); // convert int to double
//   }
// }

// class Circle extends Shape {
//   double radius;
//   Circle(this.radius);
//   @override
//   double area() {
//     return 3.14 * radius * radius;
//   }
// }

// void main() {
//   Rectangle rectangle = Rectangle(10, 20);
//   Circle circle = Circle(5);
//   print(rectangle.area());
//   print(circle.area());
// }

// abstract class Animal {
//   void makeSound();
// }

// class Dog extends Animal {
//   @override
//   void makeSound() {
//     print("Woof!");
//   }
// }

// class Cat extends Animal {
//   @override
//   void makeSound() {
//     print("Meow");
//   }
// }
// void main() {
//   Dog dog = Dog();
//   Cat cat = Cat();
//   dog.makeSound();
//   cat.makeSound();
// }

// class Flyable {
//   void fly() {
//     print("Flying");
//   }
// }

// class Bird implements Flyable {
//   @override
//   void fly() {
//     print("Flying");
//   }
// }

// class Airplane implements Flyable {
//   @override
//   void fly() {
//     print("Flying");
//   }
// }

// void main() {
//   Bird bird = Bird();
//   Airplane airplane = Airplane();
//   bird.fly();
//   airplane.fly();
// }

// mixin Logger {
//   void log(String message);
// }
// class Service with Logger{
//   @override
//   void log(String message) {
//     print(message);
//   }
// }
// void main() {
//   Service service = Service();
//   service.log("Hello");
// }
