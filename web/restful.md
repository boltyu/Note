# 指导准则
## 1.客户端服务端 Client-server
通过将用户接口和数据存储分离，提高跨平台用户接口的便携性，并且通过简化服务组件提高弹性
## 2.无状态 Stateless
每个从client到server的请求必须包含所有关于request的必要信息，且在服务端不存储关于请求的上下文
## 3.可缓存 Cacheable
缓存约束要求：响应中的数据要显式或隐式地标注是否可被缓存。如果响应可被缓存，客户端就要在之后重用响应中的数据，相当于一个请求。
## 4.统一接口 Uniform interface
为了落实软件工程中的组件接口通用原则，总体系统架构需要被简化，并且交互可视化需要提升。为了遵循统一原则，多架构约束需要引导组件特性？。
REST由4个接口约束定义：资源的identification，通过representation操作资源，sefl-descriptive消息，超媒体作为应用状态的引擎。
## 5.分层系统 Layered system
分层系统允许一个架构由受组件特性约束的多个层级组成，每个组件可以不了解与其交互的相邻层。
## 6.Code on demand (optional)
REST允许客户端功能向下拓展并执行在其框架下的代码。。。。[ori](https://restfulapi.net)
	
# 关于资源
在REST中信息抽象为资源，任何可以被命名的信息都可以是资源：文档或图片，临时服务，资源的集合，非虚拟的对象等等。REST使用resource identifier来鉴别特定资源
资源的状态在任何特定时间的已知状态即为resource representation。一个representation由数据、描述数据的元信息、超媒体链接组成，帮助客户端过渡至下一个状态。
representation的数据格式称为媒体类型media type。媒体类型决定了representation如何被处理。一个RESTful API看起来像个hypertext。每个可通过地址查找的信息单位都携带有地址，或者显式的链接和id，或者隐式的从结构中获取？

# 资源方法
很多人错误的将资源方法与HTTP方法联系起来



# REST资源命名指导
在REST中，data representation叫做资源。资源可以是单个或者集合。
'''
A resource can be a singleton or a collection. For example, “customers” is a collection resource and “customer” is a singleton resource (in a banking domain). We can identify “customers” collection resource using the URI “/customers”. We can identify a single “customer” resource using the URI “/customers/{customerId}”.

A resource may contain sub-collection resources also. For example, sub-collection resource “accounts” of a particular “customer” can be identified using the URN “/customers/{customerId}/accounts” (in a banking domain). Similarly, a singleton resource “account” inside the sub-collection resource “accounts” can be identified as follows: “/customers/{customerId}/accounts/{accountId}”.
'''
	
