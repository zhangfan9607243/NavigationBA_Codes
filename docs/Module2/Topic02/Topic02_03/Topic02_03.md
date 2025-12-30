# Topic 2.3 - 特殊的类与对象

## 1. 抽象类（Abstract Class）

抽象类是一种不能被实例化的类，它通常用作其他类的基类

- 抽象类需要通过`abc` 模块中的 `ABC` 类来定义，注意许多编程语言中是默认支持抽象类的，而 Python 需要通过 `abc` 模块来实现
- 抽象类中可以包含抽象方法，通过 `abstractmethod` 装饰器来定义，这些方法在抽象类中没有实现，必须在子类中实现

我们来看一个例子，我们可以把动物类定义为一个抽象类，然后让具体的动物类继承它：


```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "汪～"

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "喵～"
```


```python
# 以下代码会报错，因为 Animal 是抽象类，不能被实例化，大家可以取消注释试试看
# wangcai = Animal()
```


```python
wangcai = Dog("旺财")
print(wangcai.make_sound())

miaomiao = Cat("喵喵")
print(miaomiao.make_sound())
```

    汪～
    喵～


抽象类和抽象方法的逻辑其实很简单，和我们之前介绍过的覆写父类方法类似，只不过抽象的父类中的方法是没有实现的，我们就不再赘述了。

## 2. 工具类与静态方法

工具类是一种只包含静态方法的类，通常用于封装一些通用的功能

- 工具类可以被实例化，但是通常不需要实例化，而是直接使用类名就可以调用静态方法，因此也不需要初始化方法来定义属性
- 静态方法通过 `@staticmethod` 装饰器来定义，静态方法不需要访问类的实例或类本身，因此不需要传递 `self` 参数

我们来看一个例子，我们可以定义一个数学工具类，包含一些常用的数学运算方法：


```python
class MathTools:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b
```


```python
print(MathTools.add(5, 3)) 
print(MathTools.subtract(5, 3))
```

    8
    2


可以看到，我们定义了一个 `MathTools` 工具类，包含两个静态方法 `add` 和 `subtract`，用于实现加法和减法运算：

- 我们可以直接通过类名调用这些静态方法，而不需要创建类的实例
- 并且，我们在定义静态方法时，不需要初始化函数，也不需要传递 `self` 参数，因为静态方法不依赖于类的实例

这里我们简单介绍一下 `@abstractmethod` 和 `@staticmethod` 这种带 `@` 的写法：

- 这种写法叫做**装饰器（Decorator）**，是一种特殊的语法结构，用于修改函数或方法的行为
- 大家接触到的装饰器种类并不多，基本只有 `@abstractmethod` 和 `@staticmethod` 这两种，掌握固定用法就可以了，不需要掌握它的本质原理

## 3. 配置类

配置类是一种用于存储配置信息的类，通常包含一些常量属性

- 配置类通常不需要实例化，而是通过类名直接访问其属性
- 由于我们使用类名直接访问属性，因此配置类通常不需要定义初始化方法，所有的属性直接在类体缩进中定义为类属性，这个操作是大家之前没有见过的
- 配置类和工具类事实上属于两个极端：

  - 工具类通常只包含静态方法，没有属性
  - 配置类通常只包含属性，没有方法

我们来看一个例子，比方说我们要做一个游戏，我们在配置类中定义一些游戏的配置信息：

- 地图长度： 1000
- 地图宽度： 800
- 最大玩家数量： 4


```python
class Config:
    MAP_LENGTH = 1000
    MAP_WIDTH = 800
    MAX_PLAYERS = 4
```


```python
print(Config.MAP_LENGTH)
print(Config.MAP_WIDTH)
print(Config.MAX_PLAYERS)
```

    1000
    800
    4


可以看到，我们定义了一个 `Config` 配置类，包含三个类属性 `MAP_LENGTH`、`MAP_WIDTH` 和 `MAX_PLAYERS`，用于存储游戏的配置信息：

- 我们可以直接通过类名访问这些属性，而不需要创建类的实例
- 并且，我们在定义类属性时，不需要初始化函数，而是直接在类体缩进中定义，因为这些属性是类级别的，不依赖于类的实例
