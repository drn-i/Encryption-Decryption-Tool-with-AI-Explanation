from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from Algorithms import Caesar, ColumnarTrans, DiffeHellman, ElGamal, HillCipher,OneTimePad, RSA, Vigenere
from AI_Logic.TextGenerator import TextGenerator
from AI_Logic.ImageGenerator import ImageGenerator

load_dotenv()

app = FastAPI()

origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])


class CryptoRequest(BaseModel):
    algorithm: str
    operation: str
    inputText: str
    key: str
    additionalKey: Optional[str] = None

@app.post("/crypto")
def process_crypto(request: CryptoRequest):
    algorithm = request.algorithm.lower()
    operation = request.operation.lower()
    
    try:
        module = {
            'caesar': Caesar,
            'columnartrans': ColumnarTrans,
            'diffehellman': DiffeHellman,
            'elgamal': ElGamal,
            'hillcipher': HillCipher,
            'onetimepad': OneTimePad,
            'rsa': RSA,
            'vigenere': Vigenere
        }[algorithm]

        if operation == 'encrypt':
            result, steps = module.encrypt(request.inputText, request.key, request.additionalKey)
        elif operation == 'decrypt':
            result, steps = module.decrypt(request.inputText, request.key, request.additionalKey)
        else:
            raise HTTPException(status_code=404, detail="Invalid operation")


        explaination = TextGenerator(algorithm, request.inputText, request.key, operation, request.additionalKey)

        try:
            image_url = ImageGenerator(explaination)
        except Exception:
            image_url = None

        return {"result": result, "steps": steps,"explaination": explaination ,"image_url": image_url}

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
