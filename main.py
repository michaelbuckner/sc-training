import flask
from flask import request, jsonify
from waitress import serve

app = flask.Flask(__name__)
app.config['DEBUG'] = True

# Create some test data for our catalog in the form of a list of dictionaries.
transactions = [
    {'id': 0,
     'name': 'Brian Lara',
     'status': 'Active',
     'transactions': [
         {
             'transactionId': 'c3a548ca-39b7-48ca-8484-d0a45f928e53',
             'creationDate': '2020-09-16T16:27:57.557200+02:00',
             'pointOfSaleId': 'cfc0b3c7-e666-4c52-b77a-96f234b873fe',
             'contractId': '71602dd0-2790-4743-877b-e72530d7576d',
             'merchantTransactionId': 'null',
             'transactionStatus': 'SUCCESS',
             'authorizationStatus': 'SUCCESS',
             'bankCode': '0',
             'bankMessage': 'Simulated authorization',
             'authorizationCode': '000000',
             'riskScore': 'null',
             'source': 'EC',
             'description': 'null',
             'currency': 'EUR',
             'payoutCurrency': 'EUR',
             'payoutAmount': 10,
             'commission': 0,
             'fee': 0,
             'financialAccount': 'CC-CP-9933',
             'amount': 10,
             'totalAmount': 10,
             'card': {
                 'cardId': '63f046d6-d533-4cd6-a74e-1b1d75f146fc',
                 'creationDate': '2020-09-16T16:27:49.692939+02:00',
                 'customerId': 'null',
                 'cardTokenId': 'd4c7e857-b13a-4677-bfa7-348bc3df96ee',
                 'merchantCardId': 'null',
                 'commercialBrand': 'VISA',
                 'first6': '400000',
                 'last4': '0002',
                 'expirationMonth': 12,
                 'expirationYear': 2022,
                 'country': 'null',
                 'cardholderName': 'null',
                 'cardholderEmail': 'null',
                 'description': 'null',
                 'fingerprint': 'c77148952008b395b27050bed6f1b127609cb753',
                 'cardType': 'null',
                 'region': 'null',
                 'productType': 'null',
                 'europeanEconomicArea': 'null',
                 'check': 'false',
                 'additionalData': {}
             },
             'captureStatus': 'CAPTURED',
             'amountCaptured': 10,
             'refunded': 'false',
             'amountRefunded': 0,
             'refunds': [],
             'endUserIp': '245.100.1.15',
             'endUserLanguage': 'null',
             'browserUserAgent': 'null',
             'browserAcceptLanguage': 'null',
             'country': 'null',
             'receiptEmail': 'null',
             'breakdownPerSubMerchant': [],
             'transactiontransfers': [],
             'transferGroup': 'null',
             'residualAmount': 0,
             'order': {
                 'addressLine1': 'null',
                 'addressLine2': 'null',
                 'addressLine3': 'null',
                 'addressLine4': 'null',
                 'cardCountry': 'null',
                 'cardholderEmail': 'null',
                 'cardholderName': 'null',
                 'city': 'null',
                 'country': 'null',
                 'email': 'null',
                 'firstName': 'null',
                 'lastName': 'null',
                 'phone': 'null',
                 'postalCode': 'null'
             },
             'dispute': 'null',
             'authorizationCancellationDate': 'null',
             'customerId': 'null',
             'captureDate': '2020-09-16T16:27:58.125966+02:00',
             'clearingDate': 'null',
             'captureCancellationDate': 'null',
             '3ds': 'false',
             'enrollmentId': 'null',
             'movementId': 'baeb623a-4007-4acb-9497-45f5d1beb02a',
             'authorizationMovementId': '66478221-4565-46e5-af51-f176fa90275e',
             'cancelMovementId': 'null',
             'customAcceptanceData': {},
             'additionalData': {
                 'key1': 'value1',
                 'key2': 'value2'
             }
         }
     ]

     },
    {'id': 1,
     'name': 'Silvester Erik',
     'status': 'Active',
'transactions': [
         {
             'transactionId': 'c3a548ca-39b7-48ca-8484-d0a45f928e53',
             'creationDate': '2020-09-16T16:27:57.557200+02:00',
             'pointOfSaleId': 'cfc0b3c7-e666-4c52-b77a-96f234b873fe',
             'contractId': '71602dd0-2790-4743-877b-e72530d7576d',
             'merchantTransactionId': 'null',
             'transactionStatus': 'SUCCESS',
             'authorizationStatus': 'SUCCESS',
             'bankCode': '0',
             'bankMessage': 'Simulated authorization',
             'authorizationCode': '000000',
             'riskScore': 'null',
             'source': 'EC',
             'description': 'null',
             'currency': 'EUR',
             'payoutCurrency': 'EUR',
             'payoutAmount': 10,
             'commission': 0,
             'fee': 0,
             'financialAccount': 'CC-SRCC-9375',
             'amount': 10,
             'totalAmount': 10,
             'card': {
                 'cardId': '63f046d6-d533-4cd6-a74e-1b1d75f146fc',
                 'creationDate': '2020-09-16T16:27:49.692939+02:00',
                 'customerId': 'null',
                 'cardTokenId': 'd4c7e857-b13a-4677-bfa7-348bc3df96ee',
                 'merchantCardId': 'null',
                 'commercialBrand': 'VISA',
                 'first6': '400000',
                 'last4': '0002',
                 'expirationMonth': 12,
                 'expirationYear': 2022,
                 'country': 'null',
                 'cardholderName': 'null',
                 'cardholderEmail': 'null',
                 'description': 'null',
                 'fingerprint': 'c77148952008b395b27050bed6f1b127609cb753',
                 'cardType': 'null',
                 'region': 'null',
                 'productType': 'null',
                 'europeanEconomicArea': 'null',
                 'check': 'false',
                 'additionalData': {}
             },
             'captureStatus': 'CAPTURED',
             'amountCaptured': 10,
             'refunded': 'false',
             'amountRefunded': 0,
             'refunds': [],
             'endUserIp': '245.100.1.15',
             'endUserLanguage': 'null',
             'browserUserAgent': 'null',
             'browserAcceptLanguage': 'null',
             'country': 'null',
             'receiptEmail': 'null',
             'breakdownPerSubMerchant': [],
             'transactiontransfers': [],
             'transferGroup': 'null',
             'residualAmount': 0,
             'order': {
                 'addressLine1': 'null',
                 'addressLine2': 'null',
                 'addressLine3': 'null',
                 'addressLine4': 'null',
                 'cardCountry': 'null',
                 'cardholderEmail': 'null',
                 'cardholderName': 'null',
                 'city': 'null',
                 'country': 'null',
                 'email': 'null',
                 'firstName': 'null',
                 'lastName': 'null',
                 'phone': 'null',
                 'postalCode': 'null'
             },
             'dispute': 'null',
             'authorizationCancellationDate': 'null',
             'customerId': 'null',
             'captureDate': '2020-09-16T16:27:58.125966+02:00',
             'clearingDate': 'null',
             'captureCancellationDate': 'null',
             '3ds': 'false',
             'enrollmentId': 'null',
             'movementId': 'baeb623a-4007-4acb-9497-45f5d1beb02a',
             'authorizationMovementId': '66478221-4565-46e5-af51-f176fa90275e',
             'cancelMovementId': 'null',
             'customAcceptanceData': {},
             'additionalData': {
                 'key1': 'value1',
                 'key2': 'value2'
             }
         }
     ]
     },
    {'id': 2,
     'name': 'Sam Collins',
     'status': 'Active',
'transactions': [
         {
             'transactionId': 'c3a548ca-39b7-48ca-8484-d0a45f928e53',
             'creationDate': '2020-09-16T16:27:57.557200+02:00',
             'pointOfSaleId': 'cfc0b3c7-e666-4c52-b77a-96f234b873fe',
             'contractId': '71602dd0-2790-4743-877b-e72530d7576d',
             'merchantTransactionId': 'null',
             'transactionStatus': 'SUCCESS',
             'authorizationStatus': 'SUCCESS',
             'bankCode': '0',
             'bankMessage': 'Simulated authorization',
             'authorizationCode': '000000',
             'riskScore': 'null',
             'source': 'EC',
             'description': 'null',
             'currency': 'EUR',
             'payoutCurrency': 'EUR',
             'payoutAmount': 10,
             'commission': 0,
             'fee': 0,
             'financialAccount': 'CC-FCC-4577',
             'amount': 10,
             'totalAmount': 10,
             'card': {
                 'cardId': '63f046d6-d533-4cd6-a74e-1b1d75f146fc',
                 'creationDate': '2020-09-16T16:27:49.692939+02:00',
                 'customerId': 'null',
                 'cardTokenId': 'd4c7e857-b13a-4677-bfa7-348bc3df96ee',
                 'merchantCardId': 'null',
                 'commercialBrand': 'VISA',
                 'first6': '400000',
                 'last4': '0002',
                 'expirationMonth': 12,
                 'expirationYear': 2022,
                 'country': 'null',
                 'cardholderName': 'null',
                 'cardholderEmail': 'null',
                 'description': 'null',
                 'fingerprint': 'c77148952008b395b27050bed6f1b127609cb753',
                 'cardType': 'null',
                 'region': 'null',
                 'productType': 'null',
                 'europeanEconomicArea': 'null',
                 'check': 'false',
                 'additionalData': {}
             },
             'captureStatus': 'CAPTURED',
             'amountCaptured': 10,
             'refunded': 'false',
             'amountRefunded': 0,
             'refunds': [],
             'endUserIp': '245.100.1.15',
             'endUserLanguage': 'null',
             'browserUserAgent': 'null',
             'browserAcceptLanguage': 'null',
             'country': 'null',
             'receiptEmail': 'null',
             'breakdownPerSubMerchant': [],
             'transactiontransfers': [],
             'transferGroup': 'null',
             'residualAmount': 0,
             'order': {
                 'addressLine1': 'null',
                 'addressLine2': 'null',
                 'addressLine3': 'null',
                 'addressLine4': 'null',
                 'cardCountry': 'null',
                 'cardholderEmail': 'null',
                 'cardholderName': 'null',
                 'city': 'null',
                 'country': 'null',
                 'email': 'null',
                 'firstName': 'null',
                 'lastName': 'null',
                 'phone': 'null',
                 'postalCode': 'null'
             },
             'dispute': 'null',
             'authorizationCancellationDate': 'null',
             'customerId': 'null',
             'captureDate': '2020-09-16T16:27:58.125966+02:00',
             'clearingDate': 'null',
             'captureCancellationDate': 'null',
             '3ds': 'false',
             'enrollmentId': 'null',
             'movementId': 'baeb623a-4007-4acb-9497-45f5d1beb02a',
             'authorizationMovementId': '66478221-4565-46e5-af51-f176fa90275e',
             'cancelMovementId': 'null',
             'customAcceptanceData': {},
             'additionalData': {
                 'key1': 'value1',
                 'key2': 'value2'
             }
         }
     ]
     }
]


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/transactions/all', methods=['GET'])
def api_all():
    return jsonify(transactions)


serve(app, host='0.0.0.0', port=5000)
