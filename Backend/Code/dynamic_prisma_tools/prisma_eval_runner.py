import asyncio
from prisma import Prisma

async def run_prisma_query(prisma_code: str) -> list:
    """
    Run a dynamically provided Prisma ORM query and return results.
    prisma_code should be something like: 
        await db.post.find_many(where={'city': 'Kathmandu'})
    """
    db = Prisma()
    await db.connect()

    # local variables for execution context
    local_vars = {'db': db}
    try:
        # Wcompile and run the code dynamically
        exec_code = f"result = {prisma_code}"
        exec(exec_code, {}, local_vars)
        result = await local_vars['result']
    except Exception as e:
        result = {"error": str(e)}

    await db.disconnect()
    return result


# wrapper for direct calling
def run(prisma_code: str) -> list:
    return asyncio.run(run_prisma_query(prisma_code))

if __name__ == "__main__":
    code = f"""db.post.find_many(where={{'AND': [{{'address' : "kathmandu"}},{{'bedroom' : 2 }},]}})"""
    print( run(code) )
