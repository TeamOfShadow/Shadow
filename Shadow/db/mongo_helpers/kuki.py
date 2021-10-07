from Shadow.services.mongo2 import db

kukidb = db.kuki


async def is_kuki_on(chat_id: int) -> bool:
    chat = await kukidb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def kuki_on(chat_id: int):
    iz_kuki = await is_kuki_on(chat_id)
    if iz_kuki:
        return
    return await kukidb.insert_one({"chat_id": chat_id})


async def kuki_off(chat_id: int):
    iz_kuki = await is_kuki_on(chat_id)
    if not iz_kuki:
        return
    return await kukidb.delete_one({"chat_id": chat_id})
