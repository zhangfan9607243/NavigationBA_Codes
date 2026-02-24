# Topic 2.2 - 类继承的进阶用法

## 1. 多层继承和多重继承

在前面的章节中，我们介绍了比较简单场景的类继承关系，即一个子类继承自一个父类。

但是在实际的编程中，类继承关系可能会更加复杂，主要有两种情况：

- A 继承于 B，而 B 继承于 C（相当于 B 是父亲，C 是爷爷），这种情况叫做**多层继承（Multilevel Inheritance）**
- A 又继承于 B，又继承于 C（相当于 B 是父亲，C 是母亲），这种情况就叫做**多重继承（Multiple Inheritance）**
- 当然，还有多层继承和多重继承的结合情况（有爷爷有奶奶有外公有外婆有父亲有母亲）

### (1) 多层继承

#### (a) 多层继承的基本语法

多层继承的情境下，子类可以继承父类的属性和方法，同时也可以继承爷爷类的属性和方法。

我们来看以下这个例子：

- 我们先定义一个动物类 Animal
- 再一个哺乳动物类 Mammal 继承自 Animal
- 再一个狗类 Dog 继承自 Mammal
- 那么 Dog 类就可以使用 Animal 类和 Mammal 类的属性和方法

这个关系如下图所示：

```text
        Animal
           |
        Mammal
           |
          Dog
``` 


```python
class Animal:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"{self.name}是一个动物。")

class Mammal(Animal):
    def feed(self):
        print(f"{self.name}作为一个哺乳动物，它是用母乳喂养的。")

class Dog(Mammal):
    def bark(self):
        print(f"{self.name}作为一只狗，它会汪汪叫。")
```


```python
wangcai = Dog("旺财")
wangcai.intro()  # 来自 Animal 类的方法
wangcai.feed()   # 来自 Mammal 类的方法
wangcai.bark()   # 来自 Dog 类的方法
```

    旺财是一个动物。
    旺财作为一个哺乳动物，它是用母乳喂养的。
    旺财作为一只狗，它会汪汪叫。


我们上面的例子比较简单：

- 在 `Animal` 类中，我们定义了一个 `intro` 方法
- 在 `Mammal` 类中，我们定义了一个 `feed` 方法
- 在 `Dog` 类中，我们定义了一个 `bark` 方法
- 当我们创建一个 `Dog` 类的对象 `wangcai` 时，这个对象可以调用 `intro` 方法（来自 `Animal` 类），`feed` 方法（来自 `Mammal` 类），以及 `bark` 方法（来自 `Dog` 类）

#### (b) 多层继承中的同名方法

比较复杂的是以下这种情况，祖孙三代都有同名的方法：


```python
class Animal:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"{self.name}是一个动物。")

class Mammal(Animal):
    def intro(self):
        print(f"{self.name}是一个哺乳动物。")

class Dog(Mammal):
    def bark(self):
        print(f"{self.name}作为一只狗，它会汪汪叫。")
```


```python
wangcai = Dog("旺财")
wangcai.intro()
```

    旺财是一个哺乳动物。


这个情况比较复杂：

- 在 `Animal` 类中，我们定义了一个 `intro` 方法
- 在 `Mammal` 类中，我们也定义了一个 `intro` 方法（覆盖了 `Animal` 类的 `intro` 方法）
- 当我们创建一个 `Dog` 类的对象 `wangcai` 时，`wangcai` 调用的是哪个 `intro` 方法呢？我们可以看到，`wangcai` 调用的是 `Mammal` 类中的 `intro` 方法，因为在多层继承中，子类会优先使用最近的父类的方法，其实也就是就近原则。

#### (c) 多层继承中调用 `super()` 方法

之前我们介绍过 `super()` 方法，它可以用来调用父类的方法。

在多层继承中，`super()` 也可以用来调用父类的方法，但是需要注意的是，`super()` 其实也调用的是最近的父类的方法。


```python
class Animal:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"{self.name}是一个动物。")

class Mammal(Animal):
    def intro(self):
        print(f"{self.name}是一个哺乳动物。")

class Dog(Mammal):
    def bark(self):
        super().intro()
        print(f"{self.name}作为一只狗，它会汪汪叫。")
```


```python
wangcai = Dog("旺财")
wangcai.bark()
```

    旺财是一个哺乳动物。
    旺财作为一只狗，它会汪汪叫。


如果想要调用 `Animal` 类的方法，则需要在 `super()` 中加入类名和 `self` 参数，例如 `super(Mammal, self).intro()`：

- 这个代码 `super(Mammal, self)` 的意思是，要从 `Mammal` 类开始往后寻找
- 由于 MRO 顺序是 `Dog -> Mammal -> Animal`，所以从 `Mammal` 类开始往后寻找，找到的第一个 `intro` 方法就是 `Animal` 类中的 `intro` 方法
- 所以 `super(Mammal, self).intro()` 实际上调用的是 `Animal` 类中的 `intro` 方法


```python
class Animal:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"{self.name}是一个动物。")

class Mammal(Animal):
    def intro(self):
        print(f"{self.name}是一个哺乳动物。")

class Dog(Mammal):
    def bark(self):
        super(Mammal, self).intro()
        print(f"{self.name}作为一只狗，它会汪汪叫。")
```


```python
wangcai = Dog("旺财")
wangcai.bark()
```

    旺财是一个动物。
    旺财作为一只狗，它会汪汪叫。


#### (d) Python 中的方法解析顺序（Method Resolution Order, MRO）

事实上 Python 中有一个内置方法叫做 `mro()`，它可以帮助我们查看一个类的继承顺序（Method Resolution Order）

- 我们可以使用 `Dog.mro()` 来查看 `Dog` 类的继承顺序
- 注意，`mro()` 方法前面是类名，不是对象名


```python
Dog.mro()
```




    [__main__.Dog, __main__.Mammal, __main__.Animal, object]



从这个结果我们可以看到：

- 在 `Dog` 类中调用方法时，Python 会按照 `Dog` -> `Mammal` -> `Animal` 的顺序去查找方法，找到第一个匹配的方法就会调用它。
- 如果有同名的方法，Python 会首先调用 `Dog` 类中的方法
- 我们注意到 `mro()` 方法的结果中还有一个 `object`，这是因为在 Python 中，所有的类最终都会继承自一个内置的 `object` 类，这个类相当于是 Python 中所有类的祖宗类。

### (2) 多重继承

#### (a) 多重继承的基本语法

多重继承的情境下，子类可以继承多个父类的属性和方法。

多重继承的语法是：

```python
class 子类(父类1, 父类2):
    # 子类的属性和方法
```

我们来看以下这个例子：

- 我们先定义一个飞行类 Flyable，不用继承自任何类
- 我们再定义一个哺乳类 Mammal，不用继承自任何类
- 然后我们定义一个蝙蝠类 Bat，继承自 Flyable 和 Mammal
- 那么 Bat 类就可以使用 Flyable 类和 Mammal 类的属性和方法

这个关系如下图所示：

```text
      Flyable      Mammal
          \         /
           \       /
            \     /
              Bat
```


```python
class Flyable:
    def fly(self):
        print("我会飞。")

class Mammal:
    def feed(self):
        print("我是母乳喂养长大的。")

class Bat(Mammal, Flyable):
    def supersonic(self):
        print("我可以发出超声波。")
```


```python
batty = Bat()
batty.fly()      # 来自 Flyable 类的方法
batty.feed()     # 来自 Mammal 类的方法
batty.supersonic()  # 来自 Bat 类的方法
```

    我会飞。
    我是母乳喂养长大的。
    我可以发出超声波。


#### (b) 多重继承中的重名方法

如果有同名的方法，Python 会按 MRO 去查找方法，找到第一个匹配的方法就会调用它。


```python
class Flyable:
    def intro(self):
        print("我是一个会飞的动物。")

class Mammal:
    def intro(self):
        print("我是一个哺乳动物。")

class Bat(Mammal, Flyable):
    def supersonic(self):
        print("我可以发出超声波。")
```


```python
batty = Bat()
batty.intro()
```

    我是一个哺乳动物。


我们可以使用 `Bat.mro()` 来查看 `Bat` 类的继承顺序：

- 可以看到， `Bat` 类的继承顺序是 `Bat` -> `Mammal` -> `Flyable` -> `object`
- 之所以 `Mammal` 在 `Flyable` 之前，是因为在定义 `Bat` 类时，在继承的括号里，`Mammal` 被放在了 `Flyable` 的前面


```python
Bat.mro()
```




    [__main__.Bat, __main__.Mammal, __main__.Flyable, object]



#### (c) 多重继承中调用 `super()` 方法

在多重继承中，`super()` 方法的行为可能会比较复杂，因为它会按照 MRO 顺序去查找方法。


```python
class Flyable:
    def intro(self):
        print("我是一个会飞的动物。")

class Mammal:
    def intro(self):
        print("我是一个哺乳动物。")

class Bat(Mammal, Flyable):
    def supersonic(self):
        super().intro()
        print("我可以发出超声波。")
```


```python
batty = Bat()
batty.supersonic() 
```

    我是一个哺乳动物。
    我可以发出超声波。


可以看到：

- 当我们在 `Bat` 类中调用 `super().intro()` 时，实际上调用的是 `Mammal` 类中的 `intro` 方法，因为根据 MRO，`Mammal` 在 `Flyable` 之前
- 如果的确想要调用 `Flyable` 类中的 `intro` 方法，则需要在 `super()` 中加入类名和 `self` 参数，例如 `super(Mammal, self).intro()`
- 这个代码 `super(Mammal, self)` 的意思是，要从 `Mammal` 类开始往后寻找
- 由于 MRO 顺序是 `Bat -> Mammal -> Flyable`，所以从 `Mammal` 类开始往后寻找，找到的第一个 `intro` 方法就是 `Flyable` 类中的 `intro` 方法
- 所以 `super(Mammal, self).intro()` 实际上调用的是 `Flyable` 类中的 `intro` 方法


```python
class Flyable:
    def intro(self):
        print("我是一个会飞的动物。")

class Mammal:
    def intro(self):
        print("我是一个哺乳动物。")

class Cat:
    def intro(self):
        print("我是一个猫。")

class Bat(Mammal, Flyable):
    def supersonic(self):
        super(Mammal, self).intro()
        print("我可以发出超声波。")
```


```python
batty = Bat()
batty.supersonic()
```

    我是一个会飞的动物。
    我可以发出超声波。


### (3) 多层继承与多重继承的结合

当多层继承和多重继承的结合时，继承关系就会变得更加复杂

- 但是其实我们仍然可以按照 MRO 顺序去查找方法，找到第一个匹配的方法就会调用它
- 如果想要调用特定父类的方法，则可以在 `super()` 中加入类名和 `self` 参数，指定从哪个类开始往后寻找

我们来看个例子：

- 我们先定义一个动物类 Animal
- 再定义一个禽类 Bird，继承自 Animal
- 再定义一个小型动物类 SmallAnimal，继承自 Animal
- 再定义一个飞行类 Flyable，不继承自任何类
- 再定义一个游泳类 Swimmable，不继承自任何类
- 然后我们定义一个鸭子类 Duck，继承自 Bird、SmallAnimal、Flyable、Swimmable

这个关系如下图所示：

```text
            Animal
           /      \
        Bird    SmallAnimal   Flyable   Swimmable
          \        /          /           /
           \      /          /           /
            \    /          /           /
             Duck——————————/——————————–/

```


```python
class Animal:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"{self.name}是一个动物。")

class Bird(Animal):
    def intro(self):
        print("我是一个鸟类。")

class Flyable:
    def intro(self):
        print("我是一个会飞的动物。")

class Swimmable:
    def intro(self):
        print("我是一个会游泳的动物。")

class Duck(Bird, Flyable, Swimmable):
    def quack(self):
        super().intro()  # 这里调用的是哪一类的 intro 方法可能不是很明显
        print(f"{self.name}作为一只鸭子，它会嘎嘎叫。")
```

虽然此时的情景很复杂：

- 但是我们可以直接使用 `Duck.mro()` 来查看 `Duck` 类的继承顺序
- 之后，方法的调用顺序就一目了然了


```python
Duck.mro()
```




    [__main__.Duck,
     __main__.Bird,
     __main__.Animal,
     __main__.Flyable,
     __main__.Swimmable,
     object]


