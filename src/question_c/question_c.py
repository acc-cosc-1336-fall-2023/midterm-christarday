#write functions here, don't add input('') statements here!
def get_assessment_value(value):
    """
    Calculate the assessment value of a property.

    Args:
        value (float): The actual value of the property.

    Returns:
        float: The assessment value, which is 60% of the actual value.
    """
    assessment_value = value * 0.60
    return assessment_value

def get_tax_assessed(assessment_value):
    """
    Calculate the property tax based on the assessment value.

    Args:
        assessment_value (float): The assessment value of the property.

    Returns:
        float: The property tax, calculated as 72¢ for each $100 of the assessment value.
    """
    property_tax = (assessment_value / 10000) * 72
    return property_tax 