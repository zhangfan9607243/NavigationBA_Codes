# Topic 1.2 - 类和对象的基本概念

## 1. 类与对象的定义

在 Python 面相对象编程中：

- **类（Class）** 是对一类事物的抽象描述，是一种数据类型，定义了该类事物的属性和方法

    - 例如，我们接触过的列表类，它定义了列表这种数据类型的属性（如长度等）和方法（如排序等）
    - 我们还可以自定义类，例如我们可以定义一个类叫 `Cat`，它可以有属性 `color`（颜色）、`name`（名字），以及方法 `say_hello()`（喵喵叫）

- **对象（Object）** 是类的具体实例，是类的一个具体表现形式，拥有类所定义的属性和方法

    - 例如，一个具体的列表 `[1, 3, 2]` 就是列表类的一个对象，它具有列表类所定义的属性（如它的长度是 3）和方法（如它可以被排序后变成 `[1, 2, 3]`）
    - 我们可以通过自定义的类来创建对象，例如通过 `Cat` 类创建一个具体的猫对象 `tom`，它有具体的颜色和名字，并且可以调用 `say_hello()` 方法

我们可以把类比作是一个图纸，对象则是根据图纸建造出来的房子，一个图纸可以用来建造多个房子，每个房子都是图纸的一个实例。

### (1) 类的定义

在 Python 中，类通过 `class` 关键字定义，通常类名的首字母大写（驼峰命名法）：

- 在 `class 类名:` 语句下缩进的代码块中定义类的内容：规定该类对象所具有的**属性**和**方法**
- **属性**的定义是在**初始化方法**中完成的，初始化方法的名称是 `__init__`，它是一个特殊的方法，专门用于在创建对象时初始化对象的属性
- **方法**的定义则与普通函数类似，只不过这个函数专属于你定义的这个类
- 属性和方法中，一个特殊的参数就是 `self`，它表示对象本身，可以通过 `self` 访问对象的属性和其他方法

定义类的模板代码如下：

```python
class 类名:
    def __init__(self, 参数1, 参数2, ...):
        # 初始化方法，定义属性
        self.属性1 = 参数1
        self.属性2 = 参数2
        ...
    def 方法1(self, 参数):
        # 方法定义
        ...
    def 方法2(self, 参数):
        # 方法定义
```

根据这个模板，我们就来定义一个猫类 `Cat`：

- 这个类有属性 `color` 和 `name`，分别表示猫的颜色和名字
- 以及方法 `say_hello1()` 和 `say_hello2(times)`，分别表示猫打招呼和猫打招呼多次


```python
class Cat:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def say_hello1(self):
        print(f"我叫 {self.name}，喵喵！")
    
    def say_hello2(self, times):
        print(f"我叫 {self.name}，" + "喵" * times + "！")
```

这个代码写好之后，运行一下，我们这个类就定义完成了

- 和定义函数类似，定义类的时候不会有任何输出，只有在创建对象或者调用方法时才会有输出
- 下面我们就来创建这个类的对象，并调用它的方法

### (2) 创建对象

#### (a) 创建对象并查看类型

在创建对象时，直接通过类名加括号，并传入初始化方法所需的参数，注意调用的时候不用写 `self`：

```python
对象名 = 类名(初始化参数1, 初始化参数2, ...)
```

有了类 `Cat` 之后，我们就可以用这个类创建不止一个对象：

- 我们就来创建一个猫类的对象 `tom`，它的颜色是 `gray`，名字是 `Tom`
- 再来创建另一个猫类的对象 `kitty`，它的颜色是 `white`，名字是 `Kitty`


```python
# 创建对象时需要传入初始化函数所需的参数，可以写参数名
tom = Cat(color="gray", name="Tom")
```


```python
# 创建对象时也可以不写参数名，直接按顺序传入参数值，这一点和函数调用是一样的
kitty = Cat("white", "Kitty")
```

这时，我们可以验证一下，`tom` 和 `kitty` 这两个对象，确实是 `Cat` 类的实例：

- 首先，我们可以使用我们熟悉的 `type()` 函数，查看一下 `tom` 和 `kitty` 这两个对象的类型：


```python
print(type(tom))
print(type(kitty))
```

    <class '__main__.Cat'>
    <class '__main__.Cat'>


- 同时，我们还可以使用我们熟悉的 `isinstance()` 函数来检查 `tom` 和 `kitty` 是否是 `Cat` 类的实例：


```python
print(isinstance(tom, Cat))
print(isinstance(kitty, Cat))
```

    True
    True


- 调用我们熟悉的 `type()` 函数和 `isinstance()` 函数，可以看到 `tom` 和 `kitty` 确实是 `Cat` 类的实例对象，说明我们已经成功地在 Python 中创建了一个自定义的类别

#### (b) 调用对象的属性

接着，我们可以调用 `tom` 和 `kitty` 这两个对象的属性：

- 属性就是初始化函数中，通过 `self.属性名` 定义的变量
- 属性的调用直接通过 `对象名.属性名` 的方式访问，例如 `tom.name` 和 `tom.color`


```python
print(tom.name)
print(tom.color)
```

    Tom
    gray



```python
print(kitty.name)
print(kitty.color)
```

    Kitty
    white


#### (c) 调用对象的方法

我们还可以调用 `tom` 和 `kitty` 这两个对象的方法：

- 方法就是在类中定义的函数，这些函数必须带有 `self` 参数
- 方法的调用通过 `对象名.方法名(参数)` 的方式访问，例如 `tom.say_hello1()` 和 `tom.say_hello2(3)`


```python
tom.say_hello1()
tom.say_hello2(3)
```

    我叫 Tom，喵喵！
    我叫 Tom，喵喵喵！



```python
kitty.say_hello1()
kitty.say_hello2(5)
```

    我叫 Kitty，喵喵！
    我叫 Kitty，喵喵喵喵喵！


### (3) 使用内置方法来初始化属性（重要）

在上面的例子中，我们的初始化方法比较简单：

- 初始化方法中的属性，是直接传参数进去，然后赋值给属性，这样属性就被初始化了
- 但是在实际开发中，有的时候属性比较复杂，可能需要经过一些计算或者处理，才能得到最终的属性值

我们来看下面这个例子：


```python
class Person:
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.age_xu = age + 1
        self.bmi1 = self.calculate_bmi1()
        self.bmi2 = self.calculate_bmi2(weight, height)
        self.bmi3 = self.calculate_bmi2(self.weight, self.height)

    def calculate_bmi1(self):
        return self.weight / (self.height ** 2)

    def calculate_bmi2(self, weight, height):
        return weight / (height ** 2)

```


```python
zhangsan = Person("张三", 1.75, 70, 30)
print(zhangsan.age_xu)
print(zhangsan.bmi1)
print(zhangsan.bmi2)
print(zhangsan.bmi3)
```

    31
    22.857142857142858
    22.857142857142858
    22.857142857142858


在这个例子中：

- 我们定义了一个 `Person` 类，表示一个人
- 这个类有属性 `name`、`height`、`weight`、`age`、`age_xu`、`bmi1`、`bmi2`、`bmi3`
- 其中，`name`、`height`、`weight`、`age` 都是直接传参数进去赋值的属性
- 而 `age_xu` 是通过简单的计算，将传入的参数 `age` 增加 1 得到的
- 另外，`bmi1`、`bmi2`、`bmi3` 是通过调用类中的方法计算得到的：

    - `bmi1` 是通过调用 `calculate_bmi1()` 方法计算得到的：
        - 这个函数中，我们直接使用 `self.weight` 和 `self.height` 来计算 BMI 值
        - 由于初始化函数在运行到这里时，`self.weight` 和 `self.height` 已经被赋值了，所以可以直接使用

    - `bmi2` 是通过调用 `calculate_bmi2(weight, height)` 方法计算得到的：
        - 这个函数中，我们将 `weight` 和 `height` 作为参数传入，然后进行计算
        - 和 `bmi1` 的计算方式不同，这里是通过参数传递的方式来获取身高和体重
        - 也就是说，比起`calculate_bmi1`，`calculate_bmi2` 更加通用，可以计算任意给定身高和体重的 BMI 值

    - `bmi3` 也是通过调用 `calculate_bmi2(weight, height)` 方法计算得到的：
        - 只不过这里我们传进去的是，`self.weight` 和 `self.height`，也就是对象的属性值
        - 这里我们做个简单的区分：
            - `weight` 和 `height` 是初始化方法的参数，它们的作用范围仅限于初始化方法内部
            - `self.weight` 和 `self.height` 是对象的属性，不仅可以在初始化方法中使用，也可以在类的其他方法中使用，还可以被对象调用访问
            - 虽然它们的名字相同，值也相同，但它们的本质是不一样的，这个一定要注意

我们来对比一下 `calculate_bmi1` 和 `calculate_bmi2` 这两个方法在函数外的调用区别：

- `calculate_bmi1` 方法不需要传参数，直接调用即可，因为它直接使用了对象的属性 `self.weight` 和 `self.height`：


```python
print(zhangsan.calculate_bmi1())
```

    22.857142857142858


- 而 `calculate_bmi2` 方法需要传入参数 `weight` 和 `height`，这就给了这个函数在外部调用时更多的灵活性：


```python
# 张三给自己算 BMI
print(zhangsan.calculate_bmi2(zhangsan.weight, zhangsan.height))

# 张三帮李四算 BMI
print(zhangsan.calculate_bmi2(80, 1.8))

# 张三帮王五算 BMI
print(zhangsan.calculate_bmi2(60, 1.65))
```

    22.857142857142858
    24.691358024691358
    22.03856749311295


### (4) 属性与方法的简单总结

这里我们对属性与方法做个简单的总结：

- 属性：

    - **属性的定义**就是在初始化方法 `__init__` 中通过 `self.属性名 = 参数` 定义的变量
    - **属性的调用**通过 `对象名.属性名` 的方式访问，不加括号

- 方法：

    - **方法的定义**就是在类中定义的函数，这些函数必须带有 `self`
    - **方法的调用**通过 `对象名.方法名(参数)` 的方式访问，加括号并传入参数


## 2. 类的封装

其实到目前为止，我们已经体会到了类和对象的第一个特性： 封装（Encapsulation）：

- 封装强调的是，将属性和方法全都封装在类的内部，对外只暴露必要的接口，这个我们在上面定义的类的时候已经体现出来了
- 例如，在上面的 `Cat` 类中，我们将猫的属性和方法都封装在类的内部，对外只需要通过创建对象和调用方法来使用
- 这样做的好处是，可以隐藏类的内部实现细节，只暴露必要的接口，减少外部对类的依赖，提高代码的可维护性和可复用性

## 3. Python 内置的魔法方法

魔法方法（Magic Methods），也称为**特殊方法**：

- 是 Python 中以双下划线 `__` 开头和结尾的方法，这些方法在特定情况下会被自动调用，用于实现类的某些特殊行为
- 这些魔法方法都是 Python 内置的，基本的思想就是，不论你定义的类有多么复杂，它们都可以具备一些 Python 语言支持的基本特性
- 我们已经见过了 `__init__` 方法，它是用于初始化对象属性的魔法方法
- 接下来我们再来看一些其他常见的魔法方法

### (1) `__str__` 方法

`__str__` 其实就是 string 字符串的意思

- 这个方法的使用场景是，如果对象使用 `str()` 函数转换为字符串之后，字符串的内容
- 这个方法还可以用于定义，当我们使用 `print()` 函数打印对象时，显示的字符串内容
- `__str__` 方法返回的必须是一个字符串类型的值


```python
class Dog:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def bark(self):
        print(f"{self.name} 说：汪汪！")
    
    def __str__(self):
        return f"我叫{self.name}，我是一只{self.color}色狗狗。"
```


```python
snoopy = Dog("白", "Snoopy")
snoopy_str = str(snoopy)
print(snoopy_str)
```

    我叫Snoopy，我是一只白色狗狗。



```python
print(snoopy)
```

    我叫Snoopy，我是一只白色狗狗。


### (2) `__len__` 方法

`__len__` 方法用于定义当我们使用内置的 `len()` 函数获取对象的长度时，返回的值是什么。

- 我们之前接触过 Python 的组合数据类型：列表、元组、字符串等，这些数据类型都支持 `len()` 函数来获取它们的长度
- 我们自己定义的类也可以通过实现 `__len__` 方法来支持 `len()` 函数，从而返回对象的长度
- `__len__` 方法返回的必须是一个整数类型的值


```python
class Company:
    def __init__(self, employees):
        self.employees = employees

    def __len__(self):
        return len(self.employees)
```


```python
apple = Company(["张三", "李四", "王五", "赵六"])

print(len(apple))
```

    4


### (3) `__del__` 方法

`__del__` 方法用于定义当对象被 Python 的关键字 `del` 删除时，执行的操作。

- 在 Python 面向对象编程中，删除一个对象是十分常见的操作
- 例如在植物大战僵尸里，一个僵尸被消灭了，我们就可以通过 `del` 关键字将这个僵尸对象删除，从而释放内存资源，不然的话，随着游戏的进行，内存会被越来越多的僵尸对象占用，最终导致内存溢出，游戏崩溃
- 僵尸在被消灭的时候是可以执行一些操作的，比如播放一个消灭的动画，或者随机掉落一些物品，这些操作我们就可以通过 `__del__` 方法来实现


```python
class Bird:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name}飞走了。")
```


```python
shutiao = Bird("薯条")
del shutiao
```

    薯条飞走了。


### (4) 其他魔法方法

这里我们通过三个魔法方法，让大家对魔法方法有一个初步的了解。一句话总结，魔法方法就是对象在被 Python 内置的函数、关键字、或者操作符作用时，自动调用的特殊方法。

实际上 Python 内置的魔法方法还有很多，下面列举一些 专业的 Python 开发中，常见的魔法方法，如果大家以后不做专业的 Python 开发，这些方法会比较少见，这里我们就不用代码演示了：

**(a) 生命周期型**

- `__new__`：用于创建对象实例，在 `__init__` 之前调用，和 `__init__` 的区别在于 `__new__` 用于分配内存，而 `__init__` 用于初始化属性（除非专业 Python 开发，否则不用过多关注这个方法）
- `__init__`：用于初始化对象属性
- `__del__`：用于定义对象被删除时的行为

**(b) 输出型**

- `__str__`：用于定义对象的字符串表示，使用 `str()` 函数或 `print()` 函数时被调用
- `__repr__`：用于定义对象的官方字符串表示，使用 `repr()` 函数时被调用，通常用于调试（`repr()` 和 `str()` 的效果一样，都是返回字符串，但 `str()` 倾向于展示给用户看的内容，而 `repr()` 倾向于展示给开发者看的内容）

**(c) 运算型**

- `__add__`：用于定义对象的加法运算，使用 `+` 操作符时被调用
- `__sub__`：用于定义对象的减法运算，使用 `-` 操作符时被调用
- `__mul__`：用于定义对象的乘法运算，使用 `*` 操作符时被调用
- `__truediv__`：用于定义对象的除法运算，使用 `/` 操作符时被调用
- `__floordiv__`：用于定义对象的整除运算，使用 `//` 操作符时被调用
- `__mod__`：用于定义对象的取模运算，使用 `%` 操作符时被调用
- `__pow__`：用于定义对象的幂运算，使用 `**` 操作符时被调用
- `__eq__`：用于定义对象的相等比较，使用 `==` 操作符时被调用
- `__lt__`：用于定义对象的小于比较，使用 `<` 操作符时被调用
- `__gt__`：用于定义对象的大于比较，使用 `>` 操作符时被调用
- `__le__`：用于定义对象的小于等于比较，使用 `<=` 操作符时被调用
- `__ge__`：用于定义对象的大于等于比较，使用 `>=` 操作符时被调用
- `__ne__`：用于定义对象的不等比较，使用 `!=` 操作符时被调用

**(d) 容器型**

- `__len__`：用于定义对象的长度，使用 `len()` 函数时被调用
- `__getitem__`：用于定义对象的索引访问，使用 `容器[索引]` 语法时被调用
- `__setitem__`：用于定义对象的索引赋值，使用 `容器[索引] = 值` 语法时被调用
- `__delitem__`：用于定义对象的索引删除，使用 `del 容器[索引]` 语法时被调用
- `__iter__`：用于定义对象的迭代行为，使用 `for item in 容器:` 语法时被调用
- `__next__`：用于定义迭代器的下一个元素，通常与 `__iter__` 一起使用
- `__contains__`：用于定义对象的成员测试，使用 `in` 关键字时被调用

## 4. 类和对象的练习

### (1) 狗来了狗走了

- 要求：

    - 定义一个类 `Dog`，它有属性 `name` 和 `color`
    - 实现 `__init__` 方法初始化 `name` 和 `color` 属性，并且打印出“狗狗`name`来了！”
    - 实现 `__del__` 方法，当对象被删除时，打印出“狗狗`name`走了！”
    - 实现 `__str__` 方法，返回字符串“我叫`name`，我是一只`color`色狗狗。”
    - 创建一个 `Dog` 类的对象 `wangcai`，名字为“旺财”，颜色为“棕”，实现创建时、打印时、以及删除时的打印效果

- 示例代码


```python
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print(f"狗狗{self.name}来了！")
    
    def __del__(self):
        print(f"狗狗{self.name}走了！")
    
    def __str__(self):
        return f"我叫{self.name}，我是一只{self.color}色狗狗。"
```


```python
wangcai = Dog("旺财", "棕")
print(wangcai)
del wangcai
```

    狗狗旺财来了！
    我叫旺财，我是一只棕色狗狗。
    狗狗旺财走了！


### (2) 球球大作战

- 要求

    - 定义一个类 `Circle`，它有属性 `radius` 和 `color`
    - 除此之外再定义两个属性：`perimeter`（周长）和 `area`（面积），这两个属性需要通过方法计算得到
    - 创建两个 `Circle` 类的对象：
        - `ball1`，半径是随机生成的0到10之间的数，颜色为“红”
        - `ball2`，半径是随机生成的0到10之间的数，颜色为“蓝”
    - 对比一下这两个对象面积，谁大谁就胜出
    - 打印获胜信息时，要调用 `__str__` 方法，显示球的颜色

- 参考代码：


```python
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()
    
    def calculate_perimeter(self):
        import math
        return 2 * math.pi * self.radius

    def calculate_area(self):
        import math
        return math.pi * (self.radius ** 2)
    
    def __str__(self):
        return f"{self.color}球"
```


```python
import random

ball1 = Circle(random.uniform(0, 10), "红")
ball2 = Circle(random.uniform(0, 10), "蓝")

if ball1.area > ball2.area:
    print(f"{ball1}吃掉了{ball2}！")
else:
    print(f"{ball2}吃掉了{ball1}！")
```

    蓝球吃掉了红球！


### (3) 口袋妖怪打架

- 要求：

    - 定义一个类 `Pokemon`，它有属性 `name`、`hp`（血量）、`atk`（攻击力）
    - 定义两个方法 `attack(self)` 和 `defeat(self)`，分别用于攻击和被攻击
        
        - `attack(self)` 方法：打印出“`name` 发起了攻击，造成 `atk` 点伤害！”，同时返回攻击力 `atk`
        - `defeat(self, damage)` 方法：接收一个参数 `damage`，表示受到的伤害值，减少 `hp` 属性的值，并打印出“`name` 受到了 `damage` 点伤害，剩余血量 `hp`！”

    - 定义两个 `Pokemon` 类的对象：
        - `pokemon1`，名字为“皮卡丘”，血量为100，攻击力为20
        - `pokemon2`，名字为“小火龙”，血量为120，攻击力为15

    - 在一个 `while` 循环中，让两个口袋妖怪轮流攻击对方，直到其中一个口袋妖怪的血量 `hp` 小于等于0，宣布获胜者并退出循环

- 参考代码：


```python
class Pokemon:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self):
        print(f"{self.name} 发起了攻击，造成了 {self.atk} 点伤害！")
        return self.atk
    
    def defeat(self, damage):
        self.hp -= damage
        print(f"{self.name} 受到了 {damage} 点伤害，剩余 HP：{self.hp}")

pokemon1 = Pokemon("皮卡丘", 100, 20)
pokemon2 = Pokemon("小火龙", 120, 15)
```


```python
count = 1

while pokemon1.hp > 0 and pokemon2.hp > 0:
    print(f"--- 第 {count} 回合 ---")
    # 第一方攻击
    damage = pokemon1.attack()
    pokemon2.defeat(damage)
    if pokemon2.hp <= 0:
        print(f"{pokemon1.name} 胜利了！")
        break
    # 第二方攻击
    damage = pokemon2.attack()
    pokemon1.defeat(damage)
    if pokemon1.hp <= 0:
        print(f"{pokemon2.name} 胜利了！")
        break
    count += 1
```

    --- 第 1 回合 ---
    皮卡丘 发起了攻击，造成了 20 点伤害！
    小火龙 受到了 20 点伤害，剩余 HP：100
    小火龙 发起了攻击，造成了 15 点伤害！
    皮卡丘 受到了 15 点伤害，剩余 HP：85
    --- 第 2 回合 ---
    皮卡丘 发起了攻击，造成了 20 点伤害！
    小火龙 受到了 20 点伤害，剩余 HP：80
    小火龙 发起了攻击，造成了 15 点伤害！
    皮卡丘 受到了 15 点伤害，剩余 HP：70
    --- 第 3 回合 ---
    皮卡丘 发起了攻击，造成了 20 点伤害！
    小火龙 受到了 20 点伤害，剩余 HP：60
    小火龙 发起了攻击，造成了 15 点伤害！
    皮卡丘 受到了 15 点伤害，剩余 HP：55
    --- 第 4 回合 ---
    皮卡丘 发起了攻击，造成了 20 点伤害！
    小火龙 受到了 20 点伤害，剩余 HP：40
    小火龙 发起了攻击，造成了 15 点伤害！
    皮卡丘 受到了 15 点伤害，剩余 HP：40
    --- 第 5 回合 ---
    皮卡丘 发起了攻击，造成了 20 点伤害！
    小火龙 受到了 20 点伤害，剩余 HP：20
    小火龙 发起了攻击，造成了 15 点伤害！
    皮卡丘 受到了 15 点伤害，剩余 HP：25
    --- 第 6 回合 ---
    皮卡丘 发起了攻击，造成了 20 点伤害！
    小火龙 受到了 20 点伤害，剩余 HP：0
    皮卡丘 胜利了！

