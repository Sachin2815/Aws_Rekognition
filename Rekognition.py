import boto3

def detect_labels(image_path):
    aws_access_key = '****'
    aws_secret_key = '****'

    client = boto3.client('rekognition', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name='ap-south-1')

    
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    response = client.detect_labels(Image={'Bytes': image_bytes})

    return response['Labels']

def main():
    image_path = 'vimal.jpg'
    labels = detect_labels(image_path)
    
    print("Labels in the image:")
    for label in labels:
        print(f"- {label['Name']} (Confidence: {label['Confidence']:.2f}%)")

if __name__ == "__main__":
    main()
