# Topic 1.3 - 类的继承与多态

## 1. 继承的基本概念

继承是面向对象编程中的一个重要概念

- 它允许我们创建一个新类（子类），该类可以继承另一个类（父类）的属性和方法
- 通过继承，我们可以重用代码，减少重复，并且可以创建更复杂的类层次结构

### (1) 基本的继承语法

继承的语法很简单，只需在类名后面加个括号，当中指定父类名即可：

```python
class 子类名(父类名):
    子类的属性和方法
```

例如，我们可以定义一个 `Animal` 类，然后创建一个 `Dog` 类继承自 `Animal`：




```python
class Animal:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def great(self):
        return f"我是{self.name}，我是一只{self.color}色的动物。"

# Dog完全继承Animal的所有属性和方法，所以只需使用pass关键字
class Dog(Animal):
    pass
```

- 我们先来创建一个 `Animal` 实例，看下它的属性和方法：


```python
dahuang = Animal("大黄", "黄")
print(dahuang.great())
```

    我是大黄，我是一只黄色的动物。


- 我们再来创建一个 `Dog` 实例，看看它继承了哪些属性和方法：


```python
xiaobai = Dog("小白", "白")
print(xiaobai.great())
```

    我是小白，我是一只白色的动物。


可以看到，`Dog` 类直接继承了 `Animal` 类的所有属性和方法，因此：

- 我们可以在 `Dog` 类的实例上直接使用 `great` 方法，而不需要在 `Dog` 类中重新定义它
- 并且 `Dog` 类也直接继承了 `Animal` 类的 `name` 和 `color` 属性，这样在调用 `great` 方法时，就能正确地访问这些属性了

### (2) 创建子类的专属方法

如果想让子类有专属于自己的方法，可以在子类中定义它们：


```python
class Animal:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def great(self):
        return f"我是{self.name}，我是一只{self.color}色的动物。"

class Dog(Animal):
    def bark(self):
        return f"{self.name}说：汪汪汪！"

class Cat(Animal):
    def meow(self):
        return f"{self.name}说：喵喵喵！"
```


```python
laifu = Dog("来福", "棕")
print(laifu.great())
print(laifu.bark())
```

    我是来福，我是一只棕色的动物。
    来福说：汪汪汪！



```python
tom = Cat("汤姆", "灰")
print(tom.great())
print(tom.meow())
```

    我是汤姆，我是一只灰色的动物。
    汤姆说：喵喵喵！


通过上面的代码，我们可以看到：

- 如果我们想让 `Dog` 类有专属于自己的方法，就可以在 `Dog` 类中定义它们
- 而其他继承自 `Animal` 的属性和方法，`Dog` 类都可以直接使用，无需重新定义
- 同样的道理，如果我们有其他继承自 `Animal` 的子类，比如 `Cat` 类，也可以定义自己的属性和方法

当然，专属于某个子类的方法是不能在其他子类的实例上使用的：

- 比方说，`meow` 方法是 `Cat` 类专有的方法，不能在 `Dog` 类的实例上使用，也不能在 `Animal` 类的实例上使用
- 同样的，`bark` 方法是 `Dog` 类专有的方法，不能在 `Cat` 类的实例上使用，也不能在 `Animal` 类的实例上使用
- 这个概念比较简单，我们就不代码演示了

### (3) 创建子类的专属属性

如果想让子类有专属于自己的属性，则需要在 `__init__` 方法中定义它们，这其中：

- 如果是继承自父类的属性，则需要使用 `super()` 函数来调用父类的 `__init__` 方法来初始化它们
- 自己的专属属性，则可以直接在子类的 `__init__` 方法中定义
- 具体格式为：

```python
class 子类名(父类名):
    def __init__(self, 父类属性1, 父类属性2, 子类属性1, 子类属性2):
        # 调用父类的 __init__ 方法
        super().__init__(父类属性1, 父类属性2)
        # 定义子类的属性
        self.子类属性1 = 子类属性1
        self.子类属性2 = 子类属性2
```

我们来看一个例子：


```python
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def great(self):
        return f"我是{self.name}，我是一只{self.color}色的动物。"

class Dog(Animal):
    def __init__(self, name, color, breed):
        # 调用父类的构造方法初始化属性
        super().__init__(name, color)
        # 定义子类的专属属性
        self.breed = breed
    def bark(self):
        return f"{self.name}这一只{self.breed}说：汪汪汪！"
```


```python
xiaohei = Dog("小黑", "黑", "中华田园犬")
print(xiaohei.great())
print(xiaohei.bark())
```

    我是小黑，我是一只黑色的动物。
    小黑这一只中华田园犬说：汪汪汪！


这里，我们使用了 `super()` 函数来调用父类 `Animal` 的 `__init__` 方法：

- `super()` 函数的作用是调用父类的方法
- 当我们在 `Dog` 类的 `__init__` 方法中调用 `super().__init__(name, color)` 时，实际上是调用了 `Animal` 类的 `__init__` 方法
- 那么 `Animal` 类的 `__init__` 方法做了什么事儿呢？其实就是 `self.name = name` 和 `self.color = color`，也就是初始化了 `name` 和 `color` 这两个属性
- 因此，`Dog` 类的实例也就拥有了 `name` 和 `color` 这两个属性

注意：

- 使用 `super()` 函数调用父类的方法时，父类的方法中的参数也是必须传递的，否则会报错
- 如果父类的方法使用 `return` 语句返回了某个值，子类调用时就得用一个变量来接收这个返回值

## 2. 多态的基本概念

### (1) 多态的定义

多态是面向对象编程中的另一个重要概念，指的是同一个方法在不同的类中有不同的实现方式。

- 例如，`Animal` 类有一个 `make_sound` 方法，我们希望继承自这个父类的 `Dog` 类和 `Cat` 类虽然都有这个方法，但它们的实现方式不同
- `Dog` 类我们希望它实现 `make_sound` 方法时发出“汪汪”声，而 `Cat` 类我们希望它实现 `make_sound` 方法时发出“喵喵”声

多态的实现方式其实很简单，只需在子类中重写（覆盖）父类的方法即可：


```python
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def great(self):
        return f"我是{self.name}，我是一只{self.color}色的动物。"
    
    def make_sound(self):
        return "嗷呜～"

class Duck(Animal):
    def make_sound(self):
        return "嘎嘎嘎！"

class Mouse(Animal):
    def make_sound(self):
        return "吱吱吱！"
```


```python
goofy = Animal("高飞", "棕")
print(goofy.great())
print(goofy.make_sound())
```

    我是高飞，我是一只棕色的动物。
    嗷呜～



```python
donald = Duck("唐纳德", "白")
print(donald.great())
print(donald.make_sound())
```

    我是唐纳德，我是一只白色的动物。
    嘎嘎嘎！



```python
mickey = Mouse("米奇", "黑")
print(mickey.great())
print(mickey.make_sound())
```

    我是米奇，我是一只黑色的动物。
    吱吱吱！


在这个例子中：

- `Animal` 类定义了一个通用的 `make_sound` 方法，默认实现是返回“嗷呜～”

    - `goofy` 是 `Animal` 类的实例
    - 调用 `make_sound` 方法时，返回的是默认实现“嗷呜～”

- `Duck` 类重写了 `make_sound` 方法，实现为返回“嘎嘎嘎！”

    - `donald` 是 `Duck` 类的实例
    - 调用 `make_sound` 方法时，返回的是 `Duck` 类的实现“嘎嘎嘎！”

- `Mouse` 类重写了 `make_sound` 方法，实现为返回“吱吱吱！”

    - `mickey` 是 `Mouse` 类的实例
    - 调用 `make_sound` 方法时，返回的是 `Mouse` 类的实现“吱吱吱！”

这个就是**多态**的一种体现，即同一个方法 `make_sound` 在不同的类中有不同的实现方式。

### (2) 在实现多态时使用 `super()` 函数

有的时候，虽然我们想重写父类方法，但是又觉得父类中有些已经实现的功能我们还想保留

- 这时候就可以在子类的方法中使用 `super()` 函数来调用父类的方法
- 在调用了父类方法之后，子类在该方法中的特有内容，就继续补充即可

这里我们来实现一个例子：

- 父类是 `Animal`，它有一个 `run` 方法，打印 `"{name} 正在奔跑！"`，表示动物在奔跑
- 子类 `Duck` 重写了 `run` 方法，先调用父类的 `run` 方法，然后再打印 `"两条腿倒腾地特别快！"`
- 子类 `Mouse` 重写了 `run` 方法，先调用父类的 `run` 方法，然后再打印 `"四条腿倒腾地特别快！"`


```python
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def run(self):
        print(f"{self.name}正在奔跑！")

class Duck(Animal):
    def run(self):
        super().run()
        print("两条腿倒腾地特别快！")

class Mouse(Animal):
    def run(self):
        super().run()
        print("四条腿倒腾地特别快！")
```


```python
donald = Duck("唐老鸭", "白")
donald.run()
```

    唐老鸭正在奔跑！
    两条腿倒腾地特别快！



```python
mickey = Mouse("米奇", "黑")
mickey.run()
```

    米奇正在奔跑！
    四条腿倒腾地特别快！


在这个例子中：

- 当我们创建 `Duck` 类的实例 `donald` 并调用 `run` 方法时：

    - 首先会调用父类 `Animal` 的 `run` 方法，打印 `"唐老鸭正在奔跑！"`
    - 然后再执行 `Duck` 类中的专属代码，打印 `"两条腿倒腾地特别快！"`

- 当我们创建 `Mouse` 类的实例 `mickey` 并调用 `run` 方法时：

    - 首先会调用父类 `Animal` 的 `run` 方法，打印 `"米奇正在奔跑！"`
    - 然后再执行 `Mouse` 类中的专属代码，打印 `"四条腿倒腾地特别快！"`

这里我们再次总结，`super()` 函数的作用是调用父类的方法：

- 父类的方法怎么定义的，子类调用时就怎么执行
- 如果有参数，调用时就得传递参数；如果有返回值，调用时就得用变量接收返回值

这里要注意，`super()` 函数并不限于在同名的父类方法中使用：

- `super().父类方法()` 这种形式其实就是调用方法而已，方法是在哪里都可以调用的
- 所以，`super()` 可以在子类的任何方法中使用
- 我们来看一个例子，在以下例子中，`Dog` 继承自 `Animal` 类，并在自己的 `bark` 方法中使用了 `super()` 函数来调用父类的 `intro` 方法：


```python
class Animal:
    def __init__(self, name):
        self.name = name
    def intro(self):
        print("我是一个动物。")
    def make_sound(self):
        print("动物会发出声音。")

class Dog(Animal):
    def bark(self):
        super().intro()
        print("汪汪！") 

goofy = Dog("高飞")
goofy.bark()
```

    我是一个动物。
    汪汪！


## 3. 继承与多态综合练习

### (1) 鸭子和鱼游泳 - 直接打印结果的实现方式

- 要求：

    - 我们定义一个父类 `Animal`，它有一个 `swim` 方法，打印 `"{name} 正在游泳。"`
    - 然后我们定义两个子类 `Duck` 和 `Fish`，它们都继承自 `Animal` 类
    - `Duck` 类重写 `swim` 方法，先调用父类的 `swim` 方法，然后再打印 `它在水面上游来游去。"`
    - `Fish` 类重写 `swim` 方法，先调用父类的 `swim` 方法，然后再打印 `它在水下游来游去。"`

- 代码实现：


```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def swim(self):
        print(f"{self.name}正在游泳。")

class Duck(Animal):
    def swim(self):
        super().swim()
        print("它在水面上游来游去。")

class Fish(Animal):
    def swim(self):
        super().swim()
        print("它在水下游来游去。")

donald = Duck("唐老鸭")
donald.swim()

dory = Fish("多莉")
dory.swim()
```

    唐老鸭正在游泳。
    它在水面上游来游去。
    多莉正在游泳。
    它在水下游来游去。


### (2) 鸭子和鱼游泳 - 返回字符串结果的实现方式

- 要求：

    - 还是上面这个例子，鸭子和鱼游泳
    - 只不过这一次，我们不直接打印结果，而是让 `swim` 方法返回字符串结果

- 代码实现：


```python
# 返回字符串结果的实现方式
class Animal:
    def __init__(self, name):
        self.name = name
    
    def swim(self):
        return f"{self.name}正在游泳。"

class Duck(Animal):
    def swim(self):
        swim_message = super().swim()
        return f"{swim_message}\n它在水面上游来游去。"

class Fish(Animal):
    def swim(self):
        swim_message = super().swim()
        return f"{swim_message}\n它在水下游来游去。"
    
donald = Duck("唐老鸭")
print(donald.swim())

dory = Fish("多莉")
print(dory.swim())
```

    唐老鸭正在游泳。
    它在水面上游来游去。
    多莉正在游泳。
    它在水下游来游去。

