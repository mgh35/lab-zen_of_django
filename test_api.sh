curl -H "Accept: application/json" localhost:8000/posts/
curl -H "Accept: application/json" localhost:8000/posts/1/

curl -X POST -H "Accept: application/json" -d @- localhost:8000/posts/ <<EOF
{
  "title": "My Grandiose Title",
  "text": "Some really boring thing. Blah blah blah."
}
EOF
