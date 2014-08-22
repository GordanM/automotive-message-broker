#include "custompropertyinterface.h"
#include "vehicleproperty.h"
#include "varianttype.h"
#include "listplusplus.h"

CustomPropertyInterface::CustomPropertyInterface(VehicleProperty::Property prop, AbstractRoutingEngine *re, GDBusConnection *connection)
	:DBusSink(prop, re, connection, map<string, string>())
{
	PropertyList list = VehicleProperty::customProperties();

	if(contains(list,prop))
	{
		AbstractPropertyType* temp = VehicleProperty::getPropertyTypeForPropertyNameValue(prop);

		if(!temp)
		{
			throw std::runtime_error("Cannot create custom property: " + prop);
		}

		GVariant* var = temp->toVariant();
		std::string signature = g_variant_get_type_string(var);
		g_variant_unref(var);

		propertyDBusMap.push_back( new VariantType(re, prop, prop, VariantType::ReadWrite));

		delete temp;
	}


}
