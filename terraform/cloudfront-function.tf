# CloudFront Function to handle directory index rewriting for production
# This function adds index.html to requests ending with /
resource "aws_cloudfront_function" "directory_index" {
  name    = "pythoncdmx-directory-index"
  runtime = "cloudfront-js-1.0"
  comment = "Rewrites URLs ending with / to /index.html for MkDocs directory structure"
  publish = true

  code = <<-EOT
function handler(event) {
    var request = event.request;
    var uri = request.uri;

    // Check if the URI ends with '/'
    if (uri.endsWith('/')) {
        request.uri += 'index.html';
    }
    // Check if the URI doesn't have a file extension
    else if (!uri.includes('.')) {
        request.uri += '/index.html';
    }

    return request;
}
EOT
}

# CloudFront Function for staging environment
resource "aws_cloudfront_function" "directory_index_staging" {
  name    = "pythoncdmx-directory-index-staging"
  runtime = "cloudfront-js-1.0"
  comment = "Rewrites URLs ending with / to /index.html for MkDocs directory structure (Staging)"
  publish = true

  code = <<-EOT
function handler(event) {
    var request = event.request;
    var uri = request.uri;

    // Check if the URI ends with '/'
    if (uri.endsWith('/')) {
        request.uri += 'index.html';
    }
    // Check if the URI doesn't have a file extension
    else if (!uri.includes('.')) {
        request.uri += '/index.html';
    }

    return request;
}
EOT
}
