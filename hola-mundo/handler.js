const hello = async (event, context) => {
  return {
    statusCode: 200,
    body: JSON.stringify({ message: "Actualizando aplicación serverless/sls" }),
  };
};

module.exports = {
  hello,
};
