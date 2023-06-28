from fastapi import Fast Api
app=FASTAPI()
@app.get('/hellow')
async def hellow():
    return 'welcome'