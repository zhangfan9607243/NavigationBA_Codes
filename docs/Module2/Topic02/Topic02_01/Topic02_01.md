# Topic 2.1 - 类与类之间的关联与组合关系

在 Python 面向对象编程中，类与类之间的关系有3种：继承（Inheritance）、关联（Association）、与组合（Composition）。

在之前的章节中，我们已经介绍了继承关系，本节将重点讲解组合和关联关系，在这之前，我们先给大家简单区分一下关联和组合的区别：

- 关联关系（Association）：表示两个类之间存在某种联系，但它们可以独立存在：

    - 例如车和司机之间就是关联关系，司机可以开不同的车，而车也可以有不同的司机
    - 如果车被程序删除，司机依然可以存在，如果司机被程序删除，车也依然可以存在

- 组合关系（Composition）：表示一个类是另一个类的一部分，且它们的生命周期是绑定在一起的：

    - 例如车和轮子之间就是组合关系，车包含轮子，轮子不能独立于车存在
    - 如果车被程序删除，轮子也会被删除，如果轮子被程序删除，车也会受到影响

## 1. 关联关系

关联关系的一个重要特点就是：如果 A 类和 B 类之间存在关联关系，那么 A 类的对象和 B 类的对象是分别创建和删除的。

我们来看一个例子，我们模拟一下吃鸡游戏：

- 玩家类 Player，有属性 name（玩家名称），方法 shoot()（开枪）
- 武器类 Weapon，有属性 type（武器类型），方法 fire()（开火）


```python
class Player:
    def __init__(self, name):
        self.name = name
        self.weapon = None
    
    def pick_weapon(self, weapon):
        self.weapon = weapon

    def shoot(self):
        if self.weapon is not None:
            self.weapon.fire()
        else:
            print(f"{self.name}没有武器，无法射击。")

class Weapon:
    def __init__(self, type, sound):
        self.type = type
        self.sound = sound

    def fire(self):
        print(self.sound)
```


```python
zhangsan = Player("张三")
ak47 = Weapon("AK47", "咔咔咔！")
zhangsan.pick_weapon(ak47)
zhangsan.shoot()
```

    咔咔咔！



```python
lisi = Player("李四")
m16 = Weapon("M16", "Piu Piu Piu！")
lisi.pick_weapon(m16)
lisi.shoot()
```

    Piu Piu Piu！



```python
wangwu = Player("王五")
wangwu.shoot()
```

    王五没有武器，无法射击。


接着我们来尝试一下，如果讲玩家对象删除，或者武器对象删除，是否会影响到另一个对象的存在呢？

- 首先，我们尝试删除玩家对象，看看武器对象是否还能继续使用：


```python
zhaoliu = Player("赵六")
m4 = Weapon("M4", "哒哒哒！")
zhaoliu.pick_weapon(m4)
zhaoliu.shoot()

del zhaoliu
m4.fire()
```

    哒哒哒！
    哒哒哒！


- 这里我们发现，将玩家 `zhaoliu` 对象删除后，武器 `m4` 对象依然可以正常使用，说明玩家对象和武器对象是独立存在的。

- 接着我们再尝试删除武器对象，看看玩家对象是否还能继续使用：


```python
zhaoliu = Player("赵六")
m4 = Weapon("M4", "哒哒哒！")
zhaoliu.pick_weapon(m4)
zhaoliu.shoot()

del m4
zhaoliu.shoot()
```

    哒哒哒！
    哒哒哒！


- 这里我们发现，如果将武器 `m4` 对象删除后，玩家 `zhaoliu` 对象依然可以正确调用 `shoot()` 方法
- 有些同学这里可能会比较疑惑，明明 `m4` 对象被删除了，为什么 `zhaoliu` 还能调用 `shoot()` 方法呢：

    - 这是因为 `shoot()` 方法中并没有直接使用 `m4` 对象
    - 而是通过 `pick_weapon()` 方法将 `m4` 对象的引用赋值给了玩家对象的一个属性 `weapon`
    - 换句话说，在调用 `shoot()` 方法时，实际上是通过玩家对象的 `weapon.shoot()` 来调用的，而不是 `m4.shoot()`

- 所以，如果我们的目标是将 `zhaoliu` 的武器夺走，有两个方法：

    - 一是直接将 `zhaoliu.weapon` 设为 `None`，这样 `zhaoliu` 就没有武器了，调用 `shoot()` 方法时会提示没有武器
    - 二是删除 `zhaoliu.weapon`，但是这样的话，调用 `shoot()` 方法时会报错，因为 `weapon` 属性不存在了


```python
zhaoliu = Player("赵六")
m4 = Weapon("M4", "哒哒哒！")
zhaoliu.pick_weapon(m4)
zhaoliu.shoot()

zhaoliu.weapon = None
zhaoliu.shoot()
```

    哒哒哒！
    赵六没有武器，无法射击。



```python
zhaoliu = Player("赵六")
m4 = Weapon("M4", "哒哒哒！")
zhaoliu.pick_weapon(m4)
zhaoliu.shoot()

del zhaoliu.weapon
# zhaoliu.shoot() # 这一行会报错，因为 weapon 属性被删除了，大家可以取消注释试试看
```

    哒哒哒！


## 2. 组合关系

组合关系的一个重要特点是，如果 B 类是 A 类的组成部分，那么 B 类的对象将在 A 类的对象内部初始化，并且当 A 类的对象被删除时，B 类的对象也会被删除。

我们还是拿吃鸡游戏来举例：

- 载具类 Vehicle，有属性 type（载具类型），和油箱属性 fuel_tank，方法 drive()（驾驶）
- 油箱类 FuelTank，有属性 capacity（油箱容量），方法 refuel()（加油）与 consume()（消耗燃料）



```python
class FuelTank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.fuel_level = capacity  # 初始时油箱是满的

    def refuel(self, amount):
        self.fuel_level = min(self.capacity, self.fuel_level + amount)
        print(f"加油后油箱燃料水平: {self.fuel_level}/{self.capacity}")

    def consume(self, amount):
        if amount > self.fuel_level:
            print("燃料不足，无法继续行驶！") 
            self.fuel_level = 0
        else:
            self.fuel_level -= amount
            print(f"消耗燃料后油箱燃料水平: {self.fuel_level}/{self.capacity}")

class Vehicle:
    def __init__(self, type, fuel_capacity):
        self.type = type
        # 油箱对象在载具对象内部初始化
        self.fuel_tank = FuelTank(capacity=fuel_capacity)

    def drive(self, distance):
        fuel_needed = distance * 0.1  # 每公里消耗0.1单位燃料
        self.fuel_tank.consume(fuel_needed)
        if self.fuel_tank.fuel_level > 0:
            print(f"驾驶{self.type}行驶{distance}公里，消耗{fuel_needed}单位燃料。")
            
```


```python
jeep = Vehicle("吉普车", fuel_capacity=50)
print("第1次驾驶:")
jeep.drive(100)  # 驾驶100公里
jeep.fuel_tank.refuel(20)  # 加20单位燃料
print("第2次驾驶:")
jeep.drive(200)  # 再驾驶200公里
jeep.fuel_tank.refuel(50)  # 加50单位燃料
print("第3次驾驶:")
jeep.drive(1000)  # 再驾驶1000公里
```

    第1次驾驶:
    消耗燃料后油箱燃料水平: 40.0/50
    驾驶吉普车行驶100公里，消耗10.0单位燃料。
    加油后油箱燃料水平: 50/50
    第2次驾驶:
    消耗燃料后油箱燃料水平: 30.0/50
    驾驶吉普车行驶200公里，消耗20.0单位燃料。
    加油后油箱燃料水平: 50/50
    第3次驾驶:
    燃料不足，无法继续行驶！


如果我们将 `jeep` 对象删除，那么它的 `fuel_tank` 也会被删除，无法再使用：


```python
# 以下代码会报错，因为 jeep 对象已经被删除，fuel_tank 也不存在了，大家可以取消注释试试看
# del jeep
# jeep.fuel_tank.refuel(10)  
```

## 3. 关联与组合关系小结

总的来说：

- A 类和 B 类之间如果是关联关系，那么 A 类的对象和 B 类的对象是单独创建和删除的
- B 类如果是 A 类的组合部分，那么 B 类的对象将在 A 类的对象内部创建，并且当 A 类的对象被删除时，B 类的对象也会被删除

在实际的编程中，两个类别具体是关联关系还是组合关系，主要取决于它们之间的业务逻辑需求，这个是没有一个绝对标准的，需要根据具体情况来判断。
