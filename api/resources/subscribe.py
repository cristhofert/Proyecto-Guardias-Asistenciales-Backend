from models.medical_doctor import MedicalDoctorModel
from models.subscription import SubscriptionModel
from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user
from util import access

class Subscribe(Resource):
    def __init__(self):
        pass

    @jwt_required()
    def post(self, medical_doctor_id, subscription_id):
        access.administor(current_user)
        medical_doctor = MedicalDoctorModel.find_by_id(medical_doctor_id)
        subscription = SubscriptionModel.find_by_id(subscription_id)

        if medical_doctor and subscription and (medical_doctor.json()['institution'] == current_user.json()['institution']) and (subscription.json()['institution'] == current_user.json()['institution']):
            medical_doctor.subscriptions.append(subscription)

            try:
                medical_doctor.save_to_db()
            except:
                return {"message": "An error occurred inserting the subs."}, 500

            return {'medical_doctor_id': medical_doctor_id, 'subscription_id': subscription_id}, 201
        return {
            'message': 'Medical doctor or subscription not found.', 
            'subscription': subscription.json() if subscription else subscription_id,
            'medical_doctor': medical_doctor.json() if medical_doctor else medical_doctor_id
        }, 404

    @jwt_required()
    def delete(self, medical_doctor_id, subscription_id):
        access.administor(current_user)
        medical_doctor = MedicalDoctorModel.find_by_id(medical_doctor_id)
        subscription = SubscriptionModel.find_by_id(subscription_id)

        if medical_doctor and subscription and (medical_doctor.json()['institution'] == current_user.json()['institution']) and (subscription.json()['institution'] == current_user.json()['institution']):
            medical_doctor.subscriptions.revome(subscription)

            try:
                medical_doctor.save_to_db()
            except:
                return {"message": "An error occurred deleting the subs."}, 500

        return {'medical_doctor_id': medical_doctor_id, 'subscription_id': subscription_id}, 201