import asyncio
from src.launchers import _combine

WhichLaunchersExist = asyncio.run(_combine.FindLaunchers())
print(WhichLaunchersExist[0][0])
print(WhichLaunchersExist[1])

WriteToPath = asyncio.run(_combine.WritePath()) 