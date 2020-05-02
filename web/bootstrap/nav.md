# 基础导航栏
    导航.nav类是由flexbox构建的。基础.nav组件不包括任何.active状态。
    .active标注当前激活的项目，.disable使当前项目不可用
## 基础样式
    .justify-content-center 居中导航栏
                    -end 末尾（右）对齐
    .flex-column 垂直排列
    .flex-sm-column 部分？垂直排列
    .nav-tabs 为导航栏产生标签式的界面
    .nav-pills 药丸式风格
    .nav-fill 使得.nav-item将填充剩余可用空间，项目不一定等宽
    .nav-justified 同上所有水平空间被占据，不同的是每个项目等宽
    以上两种方式在使用<nav>标签时，记得要包含具有.nav-item类的子项目作为锚定