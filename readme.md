#### 介绍

#### 后端：
采用分层架构：

* controller 层负责接受 restful API 接口
* service 层负责处理业务逻辑
* dao 层负责与数据库交互
* entity 定义数据实体，负责约束数据类型以及规范
* exceptions 定义错误处理函数以及自定义的错误类型
* test 负责做一些测试

##### 数据库设计
UserTable
* userId 主键
* username 
* passwd 

TodoTable
* todoId 主键
* userId 外键
* text 事件名称
* status 状态: todo/done/delete



#### 前端
