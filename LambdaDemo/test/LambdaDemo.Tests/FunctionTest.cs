using Xunit;
using Amazon.Lambda.Core;
using Amazon.Lambda.TestUtilities;

using LambdaDemo;

namespace LambdaDemo.Tests
{

    public class FunctionTest
    {
        [Fact]
        public void TestToUpperFunction()
        {

            // Invoke the lambda function and confirm the string was upper cased.
            var function = new DemoFunction();
            var context = new TestLambdaContext();
            var upperCase = function.DemoFunctionHandler("hello world", context);

            Assert.Equal("HELLO WORLD", upperCase);
        }
    }
}