curl -X GET \
  'https://fyle-webb-app.herokuapp.com/bank_name_city?bank_name=ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED&city=MUMBAI&offset=0&limit=20' \
  -H 'authorization: JWT  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImF5dXNocGFsYWsiLCJleHAiOjE1NjE2MTY3NTYsImVtYWlsIjoiYXl1c2hwYWxha2NzQGdtYWlsLmNvbSJ9.Ae3prPvQBlWga6JJOVgXMmqFpK_PsueOX2Vd5AzXuGw' \
  -H 'cache-control: no-cache' \
  -H 'postman-token: 0040c769-fc91-d7d6-3a42-dfd5cff4632d' \
  -d '{
	"bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED",
	"city": "MUMBAI",
	"offset": "0",
	"limit": "20"
}'