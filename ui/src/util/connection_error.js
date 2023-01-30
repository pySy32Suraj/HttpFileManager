
export const connectionError = (reason, conStatusSetter) => {
    if (reason.message === "Network Error")
        conStatusSetter(false);
    else
        conStatusSetter(true);
}