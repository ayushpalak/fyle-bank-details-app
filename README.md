Getting Started

1. Get details of bank on providing bank_name, city, offset, limit

curl -X GET \
  'https://fyle-webb-app.herokuapp.com/bank_name_city?bank_name=ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED&city=MUMBAI&offset=0&limit=10' \
  -H 'authorization: JWT  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImF5dXNocGFsYWsiLCJleHAiOjE1NjE2MTY3NTYsImVtYWlsIjoiYXl1c2hwYWxha2NzQGdtYWlsLmNvbSJ9.Ae3prPvQBlWga6JJOVgXMmqFpK_PsueOX2Vd5AzXuGw' \
  -H 'cache-control: no-cache' \
  -H 'postman-token: ea8592eb-e9e6-93a8-5fd2-b691f886025d' \
  -d '{
	"bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED",
	"city": "MUMBAI",
	"offset": "0",
	"limit": "20"
}'

2. Get details of bank on providing ifsc code, offset, limit

curl -X GET \
  'https://fyle-webb-app.herokuapp.com/ifsc?ifsc=ABHY0065005&limit=10&offset=0' \
  -H 'authorization: JWT  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImF5dXNocGFsYWsiLCJleHAiOjE1NjE2MTY3NTYsImVtYWlsIjoiYXl1c2hwYWxha2NzQGdtYWlsLmNvbSJ9.Ae3prPvQBlWga6JJOVgXMmqFpK_PsueOX2Vd5AzXuGw' \
  -H 'cache-control: no-cache' \
  -H 'postman-token: a13a668c-3f5a-79ae-4a50-4dc9e6ccd0d2'
