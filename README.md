# Python 2/3 Note

<h2>1. How does Python work?</h2><br>
Python gets wirtten some code, we use some translation service called an interpreter(it will translate our code line by line) to run our code and then, our shell will spit out some instruction for our machines.<br>


<h2>2. What is a good code?</h2><br>
1. use space make code clean<br>
2. readability, is easy to understand, name does not confuse, comments <br>
3. predictability <br>
4. DRY, do not repeat again gain<br>

<h2>3. What do we need scope ?</h2><br>
why do we put everthing in global? Our machine does not have infinite memory power.<br>
Nonlocal can reduce use location in memory, once we termine our function that will destroy all variable in this function, soon we can not call variable in this function. It is nice feature in Python.<br>

<h2>3. What is the Functional Programming?</h2><br>
Functional programming is all about separation of concerns, It´s all about packaging our code into separate chunks so that everything´s well organized in each part od our code. PURE FUNCTIONS<br>

Contents
--------
**Python Types:** **[`Numbers`](#numbers)__,__[`Strings`](#strings)__,__[`Boolean`](#boolean)__,__[`Lists`](#lists)__,__[`Dictionaries`](#dictionaries)__,__ [`Tuples`](#tuples)__,__[`Sets`](#sets)__,__[`None`](#none)**  

**Python Basics:** **[`Comparison Operators`](#comparison-operators)__,__[`Logical Operators`](#logical-operators)__,__[`Loops`](#loops)__,__[`Range`](#range)__,__[`Enumerate`](#enumerate)__,__[`Counter`](#counter)__,__[`Named Tuple`](#named-tuple)__,__[`OrderedDict`](#ordereddict)**    

**Functions:** **[`Functions`](#functions)__,__[`Lambda`](#lambda)__,__[`Comprehensions`](#comprehensions)__,__[`Map,Filter,Reduce`](#map-filter-reduce)__,__[`Ternary`](#ternary-condition)__,__[`Any,All`](#any-all)__,__[`Closures`](#closures)__,__[`Scope`](#scope)**    

**Advanced Python:** **[`Modules`](#modules)__,__[`Iterators`](#iterators)__,__[`Generators`](#generators)__,__[`Decorators`](#decorators)__,__[`Class`](#class)__,__[`Exceptions`](#exceptions)__,__[`Command Line Arguments`](#command-line-arguments)__,__[`File IO`](#file-io)__,__[`Useful Libraries`](#useful-libraries)**  

<br>
<h1>Basics I</h1> <br>
1. Resume<br>
1_1. Math Function, int, float, Operator Precedence, bin(), int(string, base)<br>
1_2. Variables, expression vs statements, augmented assignment operator <br>
1_3. String, str(), Type convertion, Escape Sequence, Formatted Strings, String indexes, Immutability<br>
1_4. Built in Function, methods, len()<br>
1_5. Booleans<br>
1_6. Exercise: Type Convertion<br>
1_7. Developer Fundamentals, comments<br>
1_8. Exercise: Password Check<br>
1_9. List, Matrix, List Methods, list unpacking<br>
1_10. None<br>
1_11. Dictionary<br>
1_12. Tuple<br>
1_13. Set<br>

<h1>Basics II</h1> <br> 
2_1. Condition Logic, if elif else and ,Indentation python, Truthy and Falsy, Ternary operator<br>
2_2. Short Circuiting<br>
2_3. Loops, Iterable, range, enumerate, while, break, continue, pass<br>
2_4. GUI exercise<br>
2_5. Check for duplicates in list exercise<br>
2_6. Function, Arguments vs Parameters, Default<br>
2_7. return<br>
2_8. Methods vs Functions<br>
2_9. Docstrings, clean code, *args vs **kwarg, walrus operator, scope, global keyword, nonlocal

<h1>Developer Environment</h1><br> 
myfirstnotebook.ipynb. first try with jupyter notebook, it is so cool<br>

<h1>Advanced: Object Oriented Programming</h1><br> 
3_1. What is OOP?<br>
3_2. Create our own Object! Atrributes vs Methods, @classmethod vs @statemethod<br>
3_3. Encapsulation , Abstraction, private and public variable<br>
3_4. Inheritance Polymorphism <br>
3_5. Exercise<br>
3_6. super(), introspection<br>
3_7. Exercise<br>
3_8. Multiple Inheritance<br>
3_9. MRO<br>

<h1>Advanced: Functional Programming</h1><br> 
4_1. Pure Function(everytime modify same way), map, filter, zip, and reduce<br>
4_2. Exercise<br>
4_3. Comprehenshion<br>
4_4. Exercise<br>