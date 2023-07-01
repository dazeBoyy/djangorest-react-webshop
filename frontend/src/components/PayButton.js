import axios from "axios";
import {useSelector} from "react-redux";
import {Button} from "react-bootstrap";
import { loadStripe } from "@stripe/stripe-js";
import {ORDER_CREATE_REQUEST} from "../constants/orderConstants";




const stripePromise = loadStripe("pk_test_51NIBhsLu1cuMW26f0p4exMEnU9ZdrqqwE3LL3jEAJKuzraoRad1jC8mVusUanzx4aAGxt2E70gQPrhGJOUltuViP008ISeyiTw");
const PayButton = ({cartItems}) => {

    // PULLING OUT THE CURRENT USER WE ARE LOGGED IN AS, WE NEED TO BE LOGGED IN TO PLACE ORDER
    const { userInfo } = useSelector((state) => state.userLogin);
    console.log(userInfo.token)
    const config = {
        headers: {
            "Content-type": "application/json",
            Authorization: `Bearer ${userInfo.token}` /* PASSING IN USER TOKEN AND IF THE USER IN AUTHORISED HE'LL HAVE FULL ACCESS TO HIS PROFILE INFORMATION */,
        },
    };

    const handleCheckout = async () => {

            const response = await axios.post('/api/v1/stripe/create-checkout-session/', {
                // Pass the cart items or any other necessary data
                cartItems,
            },config).then((res) =>{
                console.log(res.data)
                if (res.data) {
                    window.location.href = res.data;
                }
            }).catch((err) => console.error(err));
            // If the response contains a URL, redirect the user to the checkout page
    };

    return (
        <>
        <Button type="submit"  variant="primary" className="w-100 " onClick={() => handleCheckout()}>Оформить заказ</Button>
        </>
    )
}
export  default PayButton