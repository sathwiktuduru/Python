# import threading
# import time

# print("Main thread started")

# def single_task():
#     print("Sub task started")
#     time.sleep(2)
#     print("Sub task completed")
# def task2():
#     for i in range(1,5):
#         if i%2==0:
#             print(i)

# thread=threading.Thread(target=single_task)
# thread2=threading.Thread(target=task2)
# thread.start()
# thread2.start()
# print("Main  thread execution is completed")    


# import threading
# import requests

# def fetch_url(url, results):
#     response = requests.get(url)
#     html_content = response.text  # Get the HTML content as a string
#     results.append(f"Fetched {url}:\n{html_content}\n")

# urls = [
#     "https://youtube.com",
#     # "https://www.python.org",
#     # "https://www.github.com"
# ]

# threads = []
# results = []

# for url in urls:
#     thread = threading.Thread(target=fetch_url, args=(url, results))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()
#     # Function to split text into chunks
#     def chunk_text(text, chunk_size=1000):
#         return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

#     # Split each fetched result into chunks and print them
#     for i, result in enumerate(results):
#         url, html_content = result.split(":\n", 1)
#         chunks = chunk_text(html_content)
#         for j, chunk in enumerate(chunks):
#             print(f"Chunk {j + 1} of {url}:\n{chunk}\n")
            
# # Display results in the console after all threads are done
# for result in results:
#     print(result)

# print("All URLs fetched")



# import queue
# import threading
# import time
# q=queue.Queue()
# def producer():
#     for i in range(5):
#         q.put(i)
#         print("Produced",i)
#         time.sleep(1)
# def consumer():
#     for i in range(5):
#         print("Consumed",q.get())
#         time.sleep(1)
# thread1=threading.Thread(target=producer)
# thread2=threading.Thread(target=consumer)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("Main thread execution completed.")



import threading
import time

def task (lock):
    with lock:
        print(f"{threading.current_thread().name} has acquired the lock")
        time.sleep(2)
        print(f"{threading.current_thread().name} has released the lock")
        
lock=threading.Lock()