Usage
=======

Example of creating a bot startup using ruythcore:

.. code-block:: python

   import ruythcore

   client = ruythcore.Client(prefix="!")
   client.run("YOUR_DISCORD_TOKEN")

Main modules
----------------
- **ruythcore.client** – Quản lý bot
- **ruythcore.commands** – Các lệnh hỗ trợ
- **ruythcore.utils** – Tiện ích mở rộng
