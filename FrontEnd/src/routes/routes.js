const Predict = () => import("@/pages/GeneralViews/Predict.vue");

const routes = [
    {
        path: "/",
        redirect: "/app",
        name: "App",
    },
    {
        path: "/app",
        component: Predict,
        name: "App",
    }
];

export default routes;
