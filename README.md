# 网上书店项目

## 项目要求

应用程序要求实现一个网上书店的基本功能，要求具有前端（用户）和后端（管理）功能，基于Web运行方式。前端具有浏览书目、购物车等功能，后端具有管理书目、基本统计功能。

## 目录结构

- e-storeDEMO：项目总目录。
  - templates：项目前端模板文件目录。用于存放前端页面模板。
    - templates/adminindex.html：管理员主页

## 说明

1. 在服务器MySQL数据库中建立名为book_store的schema

2. 在当前目录下执行如下命令进行数据库迁移

   ```
   python manage.py db init
   python manage.py db migrate
   python manage.py db upgrade
   ```

3. `python app.py`运行项目入口文件