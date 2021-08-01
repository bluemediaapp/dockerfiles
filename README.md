# Blue's dockerfiles
## How to run your own blue instance
1. Download the services. This can be done by doing `python3 setup-env.py`
2. Fill out the .env file. Format:
```env
JWT_SECRET=FILL_ME_OUT # The password protecting all your users login sessions.
```
3. Run it! Should be done by just using `docker-compose up -d --build`. Blue will now be serving on port `2865`
