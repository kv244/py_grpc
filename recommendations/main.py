#!python
# gRpc using stub created by compiler
# this actually works
# https://realpython.com/python-microservices-grpc/
# CORBA, IDL

import grpc
from recommendations_pb2_grpc import RecommendationsStub
from recommendations_pb2 import BookCategory, RecommendationRequest


request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3
)
print(request.max_results)

channel = grpc.insecure_channel("localhost:50051")
client = RecommendationsStub(channel)
request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
ret = client.Recommend(request)
print(ret)
