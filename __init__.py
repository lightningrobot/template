# 引入所需模块
from lightningrobot import Main
from lightningrobot_adapter_console import ConsoleAdapter
import lightningrobot_plugin_test
import asyncio

# 创建Adapter实例
adapter_instance = ConsoleAdapter()

# 根据GreetingPlugin的要求，创建实例时传入Adapter实例
test_plugin = lightningrobot_plugin_test.Main(adapter_instance)  # 修改这里，传入adapter_instance作为参数

# 创建包含插件的列表
plugins = [test_plugin]

# 创建Main实例并启动监听循环
main_instance = Main(adapter_instance, plugins)
asyncio.run(main_instance.start())